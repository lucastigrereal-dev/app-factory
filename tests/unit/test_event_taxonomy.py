from src.events.taxonomy import load_event_taxonomy


def test_load_event_taxonomy_list_format(tmp_path) -> None:
    """Loading an event taxonomy in list format should produce a mapping."""
    yaml_content = """
    events:
      - id: test-event
        description: "An example event"
    """
    file_path = tmp_path / "taxonomy.yaml"
    file_path.write_text(yaml_content)
    taxonomy = load_event_taxonomy(file_path)
    assert taxonomy == {"test-event": "An example event"}


def test_load_event_taxonomy_map_format(tmp_path) -> None:
    """Loading a simple mapping should return the same mapping."""
    yaml_content = """
    event.one: "First"
    event.two: "Second"
    """
    file_path = tmp_path / "taxonomy.yaml"
    file_path.write_text(yaml_content)
    taxonomy = load_event_taxonomy(file_path)
    assert taxonomy == {"event.one": "First", "event.two": "Second"}