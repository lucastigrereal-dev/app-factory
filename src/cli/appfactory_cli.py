"""
Command‑line interface for the System Creation OS (App Factory).

This script offers a starting point for executing common actions
from the command line.  It uses Typer (optional) to define commands
such as `audit`, `plan`, `validate` and `export`.  The CLI is kept
minimal and non‑destructive by default (dry‑run) and intentionally
avoids any network or deploy actions.

Example:

```bash
python -m src.cli.appfactory_cli audit --input idea_intake.json
```
"""
from __future__ import annotations

try:
    import typer
except ImportError:
    # Typer is optional; if not installed the CLI will not run.
    typer = None  # type: ignore

from pathlib import Path
import json
from ..schema import prd_output_schema  # placeholder for future imports


def audit(input_file: str) -> None:
    """Run a read‑only audit on the provided input file.

    This function currently just prints the path and checks if the file exists.
    In a future version it would call the risk classifier, schema validator and
    generate a comprehensive report.
    """
    path = Path(input_file)
    if not path.exists():
        typer.echo(f"Input file not found: {path}") if typer else print(f"Input file not found: {path}")
        return
    # Placeholder: in real code we would load the schema and validate
    typer.echo(f"Auditing {path} (read‑only)...") if typer else print(f"Auditing {path} (read‑only)...")
    # Simulate loading JSON
    try:
        with open(path, "r") as fh:
            _ = json.load(fh)
    except Exception as exc:
        typer.echo(f"Failed to parse JSON: {exc}") if typer else print(f"Failed to parse JSON: {exc}")
        return
    typer.echo("Audit complete (no schema validation implemented yet).") if typer else print("Audit complete (no schema validation implemented yet).")


def main() -> None:
    """Entrypoint for the CLI when executed as a script."""
    if typer is None:
        print("Typer not installed; CLI is unavailable.")
        return
    app = typer.Typer(help="System Creation OS CLI")
    app.command()(audit)
    app()


if __name__ == "__main__":
    main()