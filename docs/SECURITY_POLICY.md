# Security Policy

This document outlines the security principles and controls for developing and operating
the **System Creation OS**.  It complements the governance policy and validation
gates by specifying practices for protecting data, credentials and resources.

## Principles

1. **Least privilege:** Agents and modules should operate with the minimum set of
   permissions necessary to perform their tasks.  Avoid granting broad access
   rights.
2. **Separation of concerns:** Keep sensitive operations (e.g. database
   migrations, external API calls) in isolated modules.  Use explicit interfaces
   and dry‑run modes.
3. **Explicit secrets management:** Do not hardcode secrets in code or
   configuration files.  Use a secure secrets store (e.g. environment
   variables managed by a secrets manager) and provide only via the runtime
   environment.
4. **Auditability:** All sensitive actions must be logged with sufficient
   detail to reconstruct what occurred.  Logs should include timestamps,
   action descriptions and identifiers.
5. **Approval for high‑risk actions:** Operations classified as R3 must be
   approved by a human operator before execution.

## Controls

* **Access control:** Ensure that database connections use RLS policies to
  enforce tenant isolation.  API endpoints must authenticate users and
  check authorisation scopes.
* **Secure storage:** Store artefacts and configuration files in a secure
  location.  Do not expose the `/home/oai/share` directory or other sensitive
  paths to untrusted processes.
* **Network security:** Limit outbound network requests from agents.  Whitelist
  only the domains required for operation (e.g. API providers).
* **Dependency management:** Use audited dependencies and keep them up to
  date.  Monitor for known vulnerabilities in libraries and frameworks.
* **Incident response:** If a security incident is suspected, immediately
  suspend operations, preserve logs and notify the security point of contact.

---
*This policy is a starting point and should evolve as the System Creation OS
matures.*