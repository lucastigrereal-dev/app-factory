# Validation Gates

The System Creation OS enforces a series of validation gates to ensure that
artefacts meet quality standards before progressing to subsequent stages of the
pipeline.  Each gate corresponds to a checkpoint (CP) and is associated with a
risk level (R0–R3).

## CP‑0 — Informational

* **Scope:** Read‑only audits and reviews.
* **Examples:** Listing missions, reading logs, inspecting documentation.
* **Requirements:** None.  All actions at CP‑0 are classified as **R0**.

## CP‑1 — Documentation

* **Scope:** Creation or modification of internal documentation and configuration.
* **Examples:** Drafting PRDs, blueprints, schemas and YAML config files.
* **Requirements:** Artefacts must conform to their respective templates and
  schemas.  The risk level is **R1**.

## CP‑2 — Planning

* **Scope:** Generation of code scaffolds, database schemas and API contracts in dry‑run mode.
* **Examples:** Running a schema planner, creating integration stubs, generating code skeletons.
* **Requirements:** All generated artefacts must be idempotent and side effect free.
  Any attempt to execute or deploy code is prohibited.  The risk level is **R2**.

## CP‑3 — Execution

* **Scope:** Actions with external side effects such as repository creation,
  pushing commits, deploying services or triggering workflows.
* **Examples:** Creating a GitHub repository, sending an AKASHA writeback event,
  running a production workflow in n8n.
* **Requirements:** **Explicit human approval is mandatory** before performing any CP‑3 operation.
  The risk level is **R3**.

## Validation criteria

For each artefact, the following criteria should be checked at the appropriate gate:

| Artefact | Gate | Validation |
|---|---|---|
| PRD | CP‑1 | Contains sections for summary, problem, opportunity, vision and scope. |
| Blueprint | CP‑1 | Defines modules, data flows, integrations and adheres to the modular monolith pattern. |
| Schema plan | CP‑2 | Tables are normalised, keys are defined and no destructive operations. |
| API contracts | CP‑2 | Endpoints are documented with request/response schemas and error codes. |
| Code scaffold | CP‑2 | Files are created with correct naming conventions and `dry_run=True`. |
| Handoff report | CP‑1 | Summarises the mission outcome, artefacts generated and next steps. |

### Failure handling

If a validation check fails:

1. Record the failure in the error log with a clear message and context.
2. Do not progress to the next gate until the issue is resolved.
3. If the failure is at CP‑2 or CP‑3, revert any partial work and inform the operator.

Refer to `docs/ERROR_PLAYBOOK.md` for guidance on common failure scenarios.