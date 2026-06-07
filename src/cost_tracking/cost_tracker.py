"""
Cost tracking utilities for System Creation OS.

This module provides simple functions to record token usage, execution time
and estimated costs for each step in the pipeline.  It aggregates events
in memory (for demonstration purposes) and can export summary reports.

In a production environment, these functions should persist data to a
database or telemetry service.  All amounts are estimates and may not
reflect actual billing from model providers or cloud platforms.
"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional
import uuid
import time


@dataclass
class CostEvent:
    """Represents a single cost event from the factory."""
    event_id: str
    wave_id: str
    step: str
    tokens_used: int
    duration_ms: int
    model: str
    cost_usd: float
    timestamp: float = field(default_factory=lambda: time.time())


class CostTracker:
    """In‑memory cost tracker for storing and aggregating cost events."""

    def __init__(self) -> None:
        # Use a list to collect events.  In a real implementation this
        # could be a database table or telemetry sink.
        self._events: List[CostEvent] = []

    def log_event(
        self,
        wave_id: str,
        step: str,
        tokens_used: int,
        duration_ms: int,
        model: str,
        cost_usd: float,
        event_id: Optional[str] = None,
    ) -> CostEvent:
        """Log a new cost event and return the stored object.

        Args:
            wave_id: Identifier for the current mission or wave.
            step: The name of the pipeline step (e.g., "PRD", "blueprint").
            tokens_used: Number of LLM tokens consumed.
            duration_ms: Execution time in milliseconds.
            model: The model identifier used (e.g., "claude‑opus").
            cost_usd: Estimated cost in USD for this step.
            event_id: Optional pre‑defined event ID; if not provided a UUID is generated.

        Returns:
            The newly created CostEvent.
        """
        eid = event_id or str(uuid.uuid4())
        event = CostEvent(
            event_id=eid,
            wave_id=wave_id,
            step=step,
            tokens_used=tokens_used,
            duration_ms=duration_ms,
            model=model,
            cost_usd=cost_usd,
        )
        self._events.append(event)
        return event

    def get_events(self, wave_id: Optional[str] = None) -> List[CostEvent]:
        """Retrieve logged events, optionally filtered by wave ID."""
        if wave_id is None:
            return list(self._events)
        return [e for e in self._events if e.wave_id == wave_id]

    def aggregate_costs(self, wave_id: Optional[str] = None) -> Dict[str, float]:
        """Aggregate total tokens and cost for all events, optionally by wave.

        Returns a dictionary with keys `tokens`, `duration_ms` and `cost_usd`.
        """
        events = self.get_events(wave_id)
        total_tokens = sum(e.tokens_used for e in events)
        total_duration = sum(e.duration_ms for e in events)
        total_cost = sum(e.cost_usd for e in events)
        return {
            "tokens": total_tokens,
            "duration_ms": total_duration,
            "cost_usd": total_cost,
        }

    def reset(self) -> None:
        """Clear all stored events.  Useful for tests."""
        self._events.clear()


# Example usage (for demonstration; can be removed in production)
if __name__ == "__main__":
    tracker = CostTracker()
    tracker.log_event("wave‑test", "idea_intake", 5000, 10000, "claude‑sonnet", 0.10)
    tracker.log_event("wave‑test", "prd_generation", 8000, 20000, "claude‑sonnet", 0.16)
    print(tracker.aggregate_costs())