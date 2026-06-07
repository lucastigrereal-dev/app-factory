"""Event taxonomy for the System Creation OS.

This module exposes a small helper to load the event taxonomy defined in
`config/event_taxonomy.yaml`.  The taxonomy describes the canonical set of
events emitted by the App Factory.  Loading the taxonomy at runtime allows
tests to verify that events adhere to known definitions.

The YAML file should contain a mapping of event names to human‑readable
descriptions.  For example:

```yaml
app.created: "An application has been created"
prd.generated: "A product requirements document has been generated"
```

"""

from pathlib import Path
from typing import Dict

import yaml  # type: ignore


def load_event_taxonomy(path: str | Path = "config/event_taxonomy.yaml") -> Dict[str, str]:
    """Load the event taxonomy from a YAML file.

    Args:
        path: Path to the YAML file containing the taxonomy.

    Returns:
        A dictionary mapping event names to descriptions.

    Raises:
        FileNotFoundError: If the YAML file cannot be found.
        yaml.YAMLError: If the YAML is invalid.
    """
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

        # Two supported formats:
        # 1. A mapping of event names to descriptions.
        # 2. A mapping with a top‑level key ``events`` containing a list of
        #    objects with ``id`` and ``description`` keys (as seen in
        #    config/event_taxonomy.yaml).
        if isinstance(data, dict) and "events" in data and isinstance(data["events"], list):
            mapping: Dict[str, str] = {}
            for item in data["events"]:
                if isinstance(item, dict) and "id" in item and "description" in item:
                    mapping[str(item["id"])] = str(item["description"])
            return mapping

        if not isinstance(data, dict):
            raise ValueError(
                "Event taxonomy YAML must be a mapping or contain an 'events' list of id/description pairs"
            )
        return {str(k): str(v) for k, v in data.items()}