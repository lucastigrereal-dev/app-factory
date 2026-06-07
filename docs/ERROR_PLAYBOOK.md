# Error Playbook

This playbook catalogues common error scenarios that may occur while operating
the System Creation OS and provides guidance on how to handle them.  It is
intended for developers, operators and AI agents interacting with the system.

## Missing configuration

**Symptom:** A command or module complains that a required configuration file is
missing or incomplete.

**Resolution:**

1. Identify the missing file from the error message.
2. Check `FILE_MANIFEST.yaml` to confirm whether the file should exist.
3. If the file is optional, create it using a template from `config/`.
4. If the file is required, halt the operation and request input from the
   operator.

## Schema validation failure

**Symptom:** A JSON or YAML artefact fails to validate against its schema.

**Resolution:**

1. Locate the schema file in `config/` (e.g. `mission_package.schema.yaml`).
2. Use a JSON schema validator to identify which field is invalid.
3. Correct the offending value or add missing fields.
4. Re‑run the validation gate.

## Unauthorized action (R3 without approval)

**Symptom:** An attempt is made to perform a high‑risk operation (e.g.
creating a repository) without human approval.

**Resolution:**

1. Abort the operation immediately.
2. Log the attempted action with timestamp and context.
3. Notify the operator that approval is required.
4. Once approval is granted, re‑run the operation at CP‑3.

## Workflow execution error

**Symptom:** A workflow executed by n8n fails or produces an unexpected result.

**Resolution:**

1. Inspect the workflow log in n8n for error details.
2. Confirm that all API credentials and environment variables are correct.
3. Test the failing step in isolation with `dry_run=True` to reproduce the error.
4. Update the workflow specification or underlying integration code.

## AKASHA writeback failure

**Symptom:** An event intended for AKASHA memory writeback is not persisted.

**Resolution:**

1. Verify that the stub in `src/memory_writeback/akasha_writeback.py` was invoked.
2. Ensure that the event conforms to the schema defined in
   `config/akasha_writeback.schema.yaml`.
3. If writing to AKASHA is disabled (dry‑run), ensure that the event was
   logged for later replay.
4. Once the integration is live, test again in CP‑3 with human approval.

---
*This playbook is not exhaustive; update it as new error scenarios are
discovered.*