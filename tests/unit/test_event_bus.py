import builtins
from src.events.event_bus import EventBus


def test_publish_dry_run(capsys) -> None:
    """Publishing in dry‑run mode should log the event instead of invoking handlers."""
    bus = EventBus(dry_run=True)
    bus.publish("test.event", {"foo": "bar"})
    captured = capsys.readouterr()
    assert "Would publish event 'test.event'" in captured.out


def test_publish_invokes_subscribers() -> None:
    """When not in dry‑run mode the bus should call registered handlers."""
    events: list[dict] = []

    def handler(payload: dict) -> None:
        events.append(payload)

    bus = EventBus(dry_run=False)
    bus.subscribe("save", handler)
    bus.publish("save", {"x": 1})
    assert events == [{"x": 1}]