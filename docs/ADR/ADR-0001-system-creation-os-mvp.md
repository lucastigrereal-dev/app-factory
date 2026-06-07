# ADR‑0001: Minimum Viable Product Scope

## Status

Accepted – 2026‑06‑04

## Context

The initial build of the System Creation OS must demonstrate value quickly
without attempting to implement every feature envisioned for the platform.
Scope creep would jeopardise delivery and delay feedback from real users.

## Decision

We will constrain the MVP to include:

* **Core modules:** Companies, diagnostics, routines, scoring, backlog and
  integration specification.
* **PRD and blueprint generation:** The ability to produce PRDs and blueprints
  for incoming product ideas.
* **Schema and API planning:** Generating database schemas and API contracts
  in dry‑run mode.
* **Integration with n8n:** Workflows will be executed externally via n8n.  The
  FactoryOS will produce specifications but will not embed its own workflow
  engine.
* **Governance and logging:** Enforcement of risk levels and checkpoints
  throughout the process, with logs for audit purposes.

Out of scope for the MVP:

* Marketplace for templates or workflows.
* Visual workflow editor.
* Full process mining and BPMN support.
* Advanced AI agents with autonomous action.
* Mobile applications.

## Consequences

The MVP will deliver a functional core that can be used to process real
missions, generate documentation and produce integration specifications.  It
will not yet include advanced features such as a marketplace or process
mining.  Feedback from MVP users will guide prioritisation of subsequent
waves.