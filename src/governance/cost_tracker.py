"""Cost tracking utilities for the System Creation OS.

This simple class records the cumulative cost of operations.  In a real
implementation this would integrate with telemetry (e.g. Langfuse) to
capture token usage and API costs.  For now it keeps the total in memory
and logs each addition.
"""

class CostTracker:
    """Record and report execution costs."""

    def __init__(self) -> None:
        self.total: float = 0.0

    def record_cost(self, amount: float) -> None:
        """Add a cost to the running total and log it.

        Args:
            amount: The monetary cost to record.

        Returns:
            None
        """
        if amount < 0:
            raise ValueError("Cost amount cannot be negative")
        self.total += amount
        print(f"[COST] Recorded {amount:.2f}, total {self.total:.2f}")