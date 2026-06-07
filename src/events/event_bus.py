"""Event bus stub for the System Creation OS.

This module provides a minimal publish/subscribe mechanism for events during
development.  In `dry_run` mode it will simply log the events that would be
published without actually delivering them anywhere.  Once the bridge
implementations are completed, this bus can be extended to forward events
through the appropriate channels.
"""

from typing import Any, Callable, Dict, List


class EventBus:
    """Simple in‑memory event bus.

    Attributes:
        dry_run: Whether the bus should operate in dry‑run mode.  When True,
            calls to :meth:`publish` will only log events instead of
            dispatching them to handlers.
    """

    def __init__(self, dry_run: bool = True) -> None:
        self.dry_run = dry_run
        self.subscribers: Dict[str, List[Callable[[Dict[str, Any]], None]]] = {}

    def subscribe(self, event_name: str, handler: Callable[[Dict[str, Any]], None]) -> None:
        """Register a handler for a given event name.

        Args:
            event_name: Name of the event to subscribe to.
            handler: Callable that accepts the event payload.
        """
        self.subscribers.setdefault(event_name, []).append(handler)

    def publish(self, event_name: str, payload: Dict[str, Any]) -> None:
        """Publish an event to all registered handlers.

        When `dry_run` is True, this method will log the event instead of
        invoking subscribers.  If `dry_run` is False, it will call each
        handler with the provided payload.  Unknown events are ignored
        silently.

        Args:
            event_name: Name of the event being published.
            payload: Arbitrary event data.
        """
        if self.dry_run:
            print(f"[DRY RUN] Would publish event '{event_name}': {payload}")
            return

        for handler in self.subscribers.get(event_name, []):
            handler(payload)