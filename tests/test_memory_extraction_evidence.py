from services.memory.memory_extractor import _is_text_duplicate


def test_name_dedup_accepts_refinement_but_preserves_different_slots():
    assert _is_text_duplicate("User's name is Alex.", [{'text': 'Name is Alex Morgan'}])
    assert not _is_text_duplicate("User's username is alex.", [{'text': "User's name is Alex."}])
