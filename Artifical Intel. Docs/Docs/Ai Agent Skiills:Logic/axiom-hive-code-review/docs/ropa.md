# Records of Processing Activities (RoPA) Extract

**Document ID:** AXIOM-ROPA-001  
**Effective Date:** 2026-09-02  
**Controller:** axiom-hive  
**Product:** axiom-hive-code-review

---

## 1. Processing Activities

### Activity 1: Code Review via PR Diff Analysis

| Field | Value |
|-------|-------|
| **Purpose** | Provide automated code review findings on GitHub pull requests |
| **Data Categories** | PR diffs, user prompts |
| **Data Subjects** | GitHub repository contributors (whose code is reviewed) |
| **Recipients** | User only (no third-party sharing) |
| **Transfers** | GitHub API (for diff retrieval only) |
| **Retention** | Ephemeral (session only) |
| **Lawful Basis** | Contract necessity (Art. 6(1)(b) GDPR) |
| **Security Measures** | Local processing, no storage, TLS to GitHub API |
| **DPIA Required** | No |

### Activity 2: Security Monitoring (Future)

| Field | Value |
|-------|-------|
| **Purpose** | Detect abuse, prompt injection, and security incidents |
| **Data Categories** | Logs (redacted), telemetry |
| **Data Subjects** | Users of the skill |
| **Recipients** | axiom-hive only |
| **Transfers** | None (local processing) |
| **Retention** | 30 days maximum |
| **Lawful Basis** | Legitimate interests (Art. 6(1)(f) GDPR) |
| **Security Measures** | Encryption at rest, RBAC, MFA |
| **DPIA Required** | To be assessed upon implementation |

### Activity 3: Marketplace Analytics (Optional)

| Field | Value |
|-------|-------|
| **Purpose** | Improve product and customer support |
| **Data Categories** | Aggregated usage statistics, sales data |
| **Data Subjects** | Buyers/users of the skill |
| **Recipients** | Marketplace platforms (AgentPowers, Agensi, SkillExchange) |
| **Transfers** | Per marketplace terms |
| **Retention** | Per marketplace policy |
| **Lawful Basis** | Consent (where required) |
| **Security Measures** | Platform-managed |
| **DPIA Required** | No (platform-managed, anonymized) |

---

## 2. Sub-Processors

| Sub-Processor | Country | Purpose | DPA/SCCs |
|---------------|---------|---------|----------|
| GitHub | United States | PR diff retrieval | GitHub ToS |
| AgentPowers | [To be confirmed] | Marketplace distribution | Platform terms |
| Agensi | [To be confirmed] | Marketplace distribution | Platform terms |
| SkillExchange | [To be confirmed] | Marketplace distribution | Platform terms |
| Stripe | [To be confirmed] | Payment processing (Phase 4) | To be executed |

---

## 3. Data Subject Rights Procedures

| Right | Procedure | Timeline |
|-------|-----------|----------|
| **Access** | User requests export of stored data | 30 days |
| **Rectification** | User requests correction | 30 days |
| **Erasure** | User requests deletion | 30 days |
| **Restriction** | User requests processing limitation | 30 days |
| **Portability** | User requests structured export | 30 days |
| **Objection** | User objects to processing | 30 days |

**Contact for data subject requests:** [To be configured]

---

## 4. International Transfers

No international transfers occur in Phase 1. If Phase 4 (hosted MCP server) is implemented, SCCs will be executed where required.
