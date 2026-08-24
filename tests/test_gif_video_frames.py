"""Tests for GIF + video frame sampling so VL models see motion, not one frozen frame.

Covers: _gif_sample_config / _video_sample_config env resolution, GIF frame
splitting (fps + fixed + static + undecodable), video frame extraction via
ffmpeg (fps + fixed), JPEG stream splitting, mime-aware is_video_file, and
build_user_content embedding video frames as image_url blocks.
"""

import os
import subprocess
import tempfile

import pytest

from src.document_processor import (
    _gif_frames_as_jpeg,
    _gif_sample_config,
    _split_jpeg_stream,
    _video_frames_as_jpeg,
    _video_sample_config,
    build_user_content,
)
from src.upload_handler import UploadHandler


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    for key in ("GIF_SAMPLE_MODE", "GIF_FPS", "GIF_MAX_FRAMES",
                "VIDEO_SAMPLE_MODE", "VIDEO_FPS", "VIDEO_MAX_FRAMES"):
        monkeypatch.delenv(key, raising=False)
    yield


@pytest.fixture()
def gif_path(tmp_path):
    from PIL import Image
    frames = [Image.new("RGB", (64, 64), (i * 40, 255 - i * 40, 128)) for i in range(5)]
    p = tmp_path / "anim.gif"
    frames[0].save(p, save_all=True, append_images=frames[1:], duration=[200] * 5, loop=0)
    return str(p)


@pytest.fixture()
def static_gif_path(tmp_path):
    from PIL import Image
    p = tmp_path / "static.gif"
    Image.new("RGB", (32, 32), (10, 20, 30)).save(p)
    return str(p)


@pytest.fixture()
def video_path(tmp_path):
    p = tmp_path / "clip.mp4"
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i",
         "testsrc=duration=4:size=128x96:rate=10", "-pix_fmt", "yuv420p", str(p)],
        check=True,
    )
    return str(p)


class _FakeUploadHandler:
    def __init__(self, upload_dir, uploads):
        self.upload_dir = upload_dir
        self.uploads = uploads

    def _inside_upload_dir(self, path):
        return True

    def resolve_upload(self, fid, owner=None):
        return self.uploads.get(fid)

    def is_image_file(self, name, mime=""):
        return name.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".gif"))

    def is_audio_file(self, name, mime=""):
        return name.lower().endswith((".webm", ".wav", ".mp3", ".m4a", ".ogg"))

    def is_document_file(self, name, mime=""):
        return name.lower().endswith((".pdf", ".txt", ".md", ".py", ".json", ".csv", ".html"))

    def is_video_file(self, name, mime=""):
        return name.lower().endswith((".mp4", ".mov", ".mkv", ".m4v", ".avi", ".webm"))


def test_gif_sample_config_defaults():
    mode, fps, cap = _gif_sample_config()
    assert mode == "fps"
    assert fps == 1.0
    assert cap == 6


def test_gif_sample_config_env(monkeypatch):
    monkeypatch.setenv("GIF_SAMPLE_MODE", "fixed")
    monkeypatch.setenv("GIF_FPS", "2")
    monkeypatch.setenv("GIF_MAX_FRAMES", "4")
    assert _gif_sample_config() == ("fixed", 2.0, 4)
    monkeypatch.setenv("GIF_SAMPLE_MODE", "bogus")
    assert _gif_sample_config()[0] == "fps"
    monkeypatch.setenv("GIF_FPS", "nan")
    assert _gif_sample_config()[1] == 1.0
    monkeypatch.setenv("GIF_FPS", "inf")
    assert _gif_sample_config()[1] == 1.0


def test_gif_frames_fps_mode(gif_path):
    frames = _gif_frames_as_jpeg(gif_path)
    assert frames
    assert all(f.startswith(b"\xff\xd8") for f in frames)


def test_gif_frames_fixed_mode(gif_path, monkeypatch):
    monkeypatch.setenv("GIF_SAMPLE_MODE", "fixed")
    frames = _gif_frames_as_jpeg(gif_path)
    assert frames
    assert len(frames) >= 2


def test_static_gif_returns_none(static_gif_path):
    assert _gif_frames_as_jpeg(static_gif_path) is None


def test_video_sample_config_defaults():
    mode, fps, cap = _video_sample_config()
    assert mode == "fps"
    assert fps == 1.0
    assert cap == 6


def test_video_frames_fps_mode(video_path):
    frames = _video_frames_as_jpeg(video_path)
    assert frames
    assert len(frames) == 4  # 4s clip at 1 FPS
    assert all(f.startswith(b"\xff\xd8") for f in frames)


def test_video_frames_fixed_mode(video_path, monkeypatch):
    monkeypatch.setenv("VIDEO_SAMPLE_MODE", "fixed")
    frames = _video_frames_as_jpeg(video_path)
    assert frames
    assert len(frames) == 6  # capped at VIDEO_MAX_FRAMES


def test_video_frames_missing_ffmpeg(video_path, monkeypatch):
    monkeypatch.setattr("shutil.which", lambda name: None if name == "ffmpeg" else "/usr/bin/x")
    assert _video_frames_as_jpeg(video_path) is None


def test_split_jpeg_stream_roundtrip():
    data = b"junk" + b"\xff\xd8AAA\xff\xd9" + b"mid" + b"\xff\xd8BBB\xff\xd9" + b"tail"
    frames = _split_jpeg_stream(data)
    assert len(frames) == 2
    assert frames[0] == b"\xff\xd8AAA\xff\xd9"
    assert frames[1] == b"\xff\xd8BBB\xff\xd9"


def test_is_video_file_mime_aware(tmp_path):
    h = UploadHandler(str(tmp_path / "base"), str(tmp_path / "uploads"))
    assert h.is_video_file("clip.mp4", "video/mp4")
    assert h.is_video_file("clip.webm", "video/webm")
    assert not h.is_video_file("clip.webm", "audio/webm")
    assert h.is_video_file("clip.mkv")
    assert not h.is_video_file("song.mp3", "audio/mpeg")
    assert not h.is_video_file("pic.png", "image/png")


def test_build_user_content_video_frames(tmp_path):
    vid = tmp_path / "clip.mp4"
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i",
         "testsrc=duration=3:size=128x96:rate=10", "-pix_fmt", "yuv420p", str(vid)],
        check=True,
    )
    h = _FakeUploadHandler(str(tmp_path), {"vid1": {
        "path": str(vid), "name": "clip.mp4", "mime": "video/mp4", "original_name": "clip.mp4",
    }})
    content = build_user_content("hello", ["vid1"], str(tmp_path), h, owner="test")
    assert isinstance(content, list)
    images = [b for b in content if b.get("type") == "image_url"]
    assert len(images) >= 2
    assert all(b["image_url"]["url"].startswith("data:image/jpeg;base64,") for b in images)


def test_build_user_content_video_fallback_no_frames(tmp_path, monkeypatch):
    vid = tmp_path / "clip.mp4"
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i",
         "testsrc=duration=1:size=64x48:rate=5", "-pix_fmt", "yuv420p", str(vid)],
        check=True,
    )
    h = _FakeUploadHandler(str(tmp_path), {"vid1": {
        "path": str(vid), "name": "clip.mp4", "mime": "video/mp4", "original_name": "clip.mp4",
    }})
    monkeypatch.setattr("shutil.which", lambda name: None if name == "ffmpeg" else "/usr/bin/x")
    content = build_user_content("hello", ["vid1"], str(tmp_path), h, owner="test")
    text = content[0]["text"] if isinstance(content, list) else content
    assert "Video attached" in text
