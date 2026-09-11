# Security Policy

**Document ID:** AXIOM-SECURITY-001  
**Effective Date:** 2026-09-02  
**Product:** axiom-hive-code-review  
**Owner:** Nicholas Michael Grossi

---

## 1. Purpose

This policy defines security controls for the `axiom-hive-code-review` skill and associated infrastructure.

## 2. Scope

- Skill files and scripts in the repository
- MCP server (Phase 4, when implemented)
- Distribution channels (marketplaces, direct sales)
- Administrative access to repository and hosting platforms

## 3. Identity and Access Management

- MFA required for all administrative accounts.
- RBAC enforced with least privilege.
- Periodic access reviews (annual minimum).
- No shared accounts.

## 4. Application and Infrastructure Security

- Secrets management: No secrets in code or logs.
- Network segmentation: Isolate production components from development.
- WAF and rate limiting: Implemented for MCP server (Phase 4).
- DDoS protection: Provided by hosting platform (Cloudflare Workers / Vercel).

## 5. Vulnerability Management

- Regular scanning: SAST, DAST, dependency scanning.
- Patch SLAs:
  - Critical: 7 days
  - High: 30 days
  - Medium: 90 days
  - Low: Next release
- Coordinated vulnerability disclosure: security@nicholasmgrossi.example (to be configured).

## 6. Incident Response

- Documented IR plan with roles, escalation, and communication templates.
- GDPR breach notification: 72-hour supervisory authority notification where required.
- Post-incident review and corrective actions within 30 days.

## 7. Secure Development

- Threat modeling for prompt injection, data exfiltration, and model misuse.
- Code review for all changes.
- No personal data or secrets in logs.
- Input validation in all scripts and MCP tools.

## 8. Monitoring and Logging

- Privacy-preserving logging by default.
- Logs retained for 30 days maximum.
- No personal data in logs.
