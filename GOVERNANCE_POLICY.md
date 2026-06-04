# Governance Policy

This document defines the governance model for operating and extending the System Creation OS.
It is derived from the canonical definitions in `SYSTEM_CANON.md` and the risk model
described throughout the project documentation.

## Risk levels

The System Creation OS classifies all actions according to four discrete risk levels:

| Risk | Description | Examples |
|---|---|---|
| **R0 – Read‑only** | Actions that only read data or documentation, with no possibility of side effects. | Listing files, reading configuration, running unit tests with `--dry‑run`.
| **R1 – Low risk write** | Actions that create or modify documents or configuration files without interacting with external systems. | Generating a PRD, updating a markdown file, producing a JSON contract.
| **R2 – Planned code** | Actions that involve generating code or planning infrastructure but do not execute it.  All code is created in dry‑run mode by default. | Generating a database schema plan, drafting integration code, scaffolding a repository structure without pushing.
| **R3 – High risk / side effect** | Actions that interact with external systems, trigger deployments, create repositories or write to remote services.  **R3 actions require explicit human approval**. | Creating a GitHub repository, running deployment scripts, executing workflows against a live n8n instance.

## Prohibited actions

The following actions are prohibited by default and require a corresponding policy waiver before they can be executed:

* Performing automatic deployments or pushes without an approved checkpoint (CP‑3).
* Reading from or writing to any `.env` or secret files via an agent.
* Running `git add -A` or any command that stages all changes without an explicit path.
* Creating a new automation factory before the existing factories have been integrated.
* Modifying production data when operating in `dry_run=True` mode.

## Checkpoint gates (CP‑n)

In addition to risk levels, the System Creation OS uses explicit checkpoint gates to ensure that
critical transitions are reviewed:

| Gate | Purpose | Typical actions |
|---|---|---|
| **CP‑0** | Informational checkpoint; everything is read‑only. | Running audits, reviewing logs.
| **CP‑1** | Low‑risk creation; documentation and configuration only. | Generating PRDs and blueprints.
| **CP‑2** | Medium‑risk planning; code generation in dry‑run mode. | Drafting scaffolds, producing schema plans.
| **CP‑3** | High‑risk execution; side effects allowed only after human approval. | Creating repositories, pushing commits, deploying services.

## Default settings

Unless otherwise specified, every module or command should run with `dry_run=True`.  This ensures that
no side effects occur without explicit consent.  Agents and commands must enforce risk checks
and record their intent in logs.  Any attempt to perform an R3 action must require explicit
acknowledgement from a human operator.

## Revision and ADRs

Changes to this policy must be recorded in a corresponding ADR (Architecture Decision Record) stored
under `docs/ADR/`.  The `SYSTEM_CANON.md` file is the highest authority for the overall definition of
the System Creation OS.  If an update conflicts with the canon, an ADR must accompany the change to
justify the divergence.