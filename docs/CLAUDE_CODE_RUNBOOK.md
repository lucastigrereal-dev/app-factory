# Claude Code Runbook

This runbook provides guidance for using **Claude Code** with the
System Creation OS file pack.  It explains how to ingest the pack,
interpret its contents and perform actions safely.

## 1. Setup

1. **Extract the file pack:** Unzip `system-creation-os-file-pack-v2.zip` into a working directory.  The top‑level
   directory contains documentation, configuration, examples and placeholders.
2. **Read the canon and state:** Begin by reading `SYSTEM_CANON.md` to understand the canonical
   definition and `SYSTEM_STATE.md` to see the current operational status.
3. **Review the manifest:** Consult `FILE_MANIFEST.yaml` for an inventory of files and their
   risk classifications.

## 2. Operating guidelines

* **Dry‑run by default:** All commands executed by Claude Code should use a `dry_run=True` parameter when
  available.  This ensures that no side effects occur during planning or testing.
* **Risk levels:** Before performing an action, classify it as R0–R3 (see
  `GOVERNANCE_POLICY.md`).  Claude Code must not perform R3 actions without
  explicit human approval.
* **Checkpoints:** Use CP‑1 for creating documentation, CP‑2 for generating plans and code, and CP‑3 for
  any operation that writes to external systems or creates repositories.
* **Explicit paths:** Avoid `git add -A` or globbing.  Specify explicit file paths when staging commits or
  updating files.

## 3. Common workflows

### Creating a PRD

1. Use the `docs/PRD.md` template as a starting point.
2. Populate the fields (summary, problem, opportunity, vision) based on
   input from the idea intake phase.
3. Save the file under `docs/products/<product_name>/PRD.md` (create the directory
   if needed) and update the manifest accordingly.

### Generating a blueprint

1. Review the architecture in `docs/ARCHITECTURE.md` and the patterns from
   the blueprint in `docs/BLUEPRINT.md`.
2. Create a new YAML file under `docs/products/<product_name>/blueprint.yaml` describing
   the system modules, data stores and external integrations.
3. Ensure that the blueprint adheres to the modular monolith and integration
   runtime architecture.

### Planning a schema

1. Draft a SQL plan in a `.sql` file referencing relevant tables (companies, routines, etc.).
2. Use dry‑run migrations or schema planners to validate the plan.
3. Save the plan under `docs/products/<product_name>/schema_plan.sql`.

### Updating AKASHA and KRATOS

1. After completing a mission, emit an AKASHA writeback event by calling the stub
   in `src/memory_writeback/akasha_writeback.py` with appropriate payload.  In dry‑run mode,
   this will log the event instead of writing.
2. Send a KRATOS snapshot using `src/api/kratos_status.py` to update the external
   status dashboard.

## 4. Error handling

Errors encountered during code execution or plan generation should be logged and
reported back to the operator.  Do not ignore exceptions or suppress tracebacks.  Refer
to `docs/ERROR_PLAYBOOK.md` for a list of common failure modes and recovery steps.

## 5. Continual improvement

After each mission, update the relevant documents (e.g. PRD, blueprint, schemas) and
commit the changes.  Record any lessons learned in `SYSTEM_STATE.md` under
“Histórico de Updates”.

---
*This runbook is a living document and should evolve alongside the System Creation OS.*