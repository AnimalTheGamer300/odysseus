"""Image-domain tool implementations.

Extracted from tool_implementations.py as part of slice 1 (#4082/#4071).
Holds the edit_image (gallery) and fetch_image tools.
``src.tool_implementations`` re-exports these for backward compatibility.
``_INTERNAL_BASE`` still lives in tool_implementations.py and is pulled back
function-locally here.
"""
import base64
import mimetypes
from pathlib import Path
from typing import Dict, Optional

import httpx

from src.tools._common import _parse_tool_args


async def do_fetch_image(content: str, owner: Optional[str] = None) -> Dict:
    """Fetch an image from a URL or local path for vision analysis.

    Returns ``image_data_url`` (data: URL) so the agent loop can inject it
    as a vision message in the next round. Pass save_to_gallery=true to
    also store it in the user's gallery.
    """
    try:
        args = _parse_tool_args(content)
    except ValueError:
        return {"error": "Invalid JSON arguments", "exit_code": 1}

    url = args.get("url", "")
    path = args.get("path", "")
    save_to_gallery = bool(args.get("save_to_gallery", False))

    if not url and not path:
        return {"error": "url or path is required", "exit_code": 1}

    try:
        if url:
            async with httpx.AsyncClient(timeout=60) as client:
                resp = await client.get(url, follow_redirects=True)
                resp.raise_for_status()
                raw = resp.content
                content_type = resp.headers.get("content-type", "").split(";")[0].strip() or "application/octet-stream"
                suggested_name = Path(url).name or "fetched_image"
        else:
            p = Path(path).expanduser()
            if not p.is_file():
                return {"error": f"Image file not found: {path}", "exit_code": 1}
            raw = p.read_bytes()
            content_type = mimetypes.guess_type(str(p))[0] or "application/octet-stream"
            suggested_name = p.name

        if not content_type or not content_type.startswith("image/"):
            return {"error": f"Not an image: {content_type}", "exit_code": 1}

        b64 = base64.b64encode(raw).decode("ascii")
        image_data_url = f"data:{content_type};base64,{b64}"

        result: Dict = {
            "output": f"Fetched image ({suggested_name}, {len(raw)} bytes)",
            "exit_code": 0,
            "image_data_url": image_data_url,
            "image_url": image_data_url,
            "image_name": suggested_name,
            "image_size": len(raw),
        }

        if save_to_gallery:
            from src.database import GalleryImage, SessionLocal
            db = SessionLocal()
            try:
                img = GalleryImage(
                    filename=suggested_name,
                    prompt=args.get("prompt", ""),
                    model="fetch_image",
                    size=str(len(raw)),
                    quality="",
                    owner=owner,
                )
                db.add(img)
                db.commit()
                db.refresh(img)
                result["image_id"] = img.id
                result["gallery_saved"] = True
            except Exception as e:
                db.rollback()
                result["gallery_error"] = str(e)
            finally:
                db.close()

        return result

    except Exception as e:
        return {"error": str(e), "exit_code": 1}


async def do_edit_image(content: str, owner: Optional[str] = None) -> Dict:
    """Edit a gallery image (upscale, rembg, inpaint, harmonize)."""
    import httpx
    from src.tool_implementations import _INTERNAL_BASE  # shared constant, still lives in the facade
    try:
        args = _parse_tool_args(content)
    except ValueError:
        return {"error": "Invalid JSON arguments", "exit_code": 1}
    image_id = args.get("image_id", "")
    action = args.get("action", "")
    if not image_id or not action:
        return {"error": "image_id and action are required", "exit_code": 1}
    payload = {"image_id": image_id}
    if args.get("prompt"):
        payload["prompt"] = args["prompt"]
    if args.get("scale"):
        payload["scale"] = args["scale"]
    try:
        async with httpx.AsyncClient(timeout=120) as client:
            resp = await client.post(f"{_INTERNAL_BASE}/api/gallery/{action}", json=payload)
            data = resp.json()
        new_id = data.get("id") or data.get("image_id")
        if data.get("success") or new_id:
            result = {
                "output": f"Image edited ({action}). New image ID: {new_id or '?'}",
                "exit_code": 0,
            }
            if new_id:
                result["image_id"] = new_id
                try:
                    from src.database import GalleryImage, SessionLocal
                    db = SessionLocal()
                    try:
                        q = db.query(GalleryImage).filter(GalleryImage.id == new_id)
                        if owner:
                            q = q.filter(GalleryImage.owner == owner)
                        img = q.first()
                        if img and img.filename:
                            result.update({
                                "image_url": f"/api/generated-image/{img.filename}",
                                "image_prompt": img.prompt or args.get("prompt") or action,
                                "image_model": img.model or "edit_image",
                                "image_size": img.size or "",
                                "image_quality": img.quality or "",
                            })
                    finally:
                        db.close()
                except Exception:
                    pass
            return result
        return {"error": data.get("error", f"{action} failed"), "exit_code": 1}
    except Exception as e:
        return {"error": str(e), "exit_code": 1}
