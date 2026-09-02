# Axiom Hive Code Review — Compliance Documentation

**Document ID:** AXIOM-COMPLIANCE-001  
**Effective Date:** 2026-09-02  
**Product:** axiom-hive-code-review  
**Owner:** axiom-hive  
**Classification:** Public / Non-Sensitive  
**Review Cycle:** Annual or upon material change

---

## 1. Purpose and Scope

This document establishes the compliance framework for the `axiom-hive-code-review` AI skill. It defines mandatory requirements aligned to:

- **GDPR** (EU General Data Protection Regulation, Regulation (EU) 2016/679)
- **NIST Privacy Framework** and **NIST Cybersecurity Framework 2.0**
- **EU AI Act** (risk-based obligations, transparency, governance)

### 1.1 Scope

This specification applies to all interactions, processing, and distribution activities related to the skill, including:

- Q&A, drafting, summarization, planning, and technical guidance delivered through the skill
- Handling of prompts, outputs, and any incidental data processed during skill execution
- Distribution via marketplaces, direct sales, and MCP server deployment

### 1.2 Non-Goals

This assistant skill does not provide legal advice, medical diagnosis, or professional certification. It does not act as a substitute decision-maker for high-impact domains (employment, housing, credit, insurance, education admissions, law enforcement, migration, or health triage) unless explicitly designed, assessed, and authorized under applicable law and governance.

---

## 2. Normative References

| Reference | Title | Relevance |
|-----------|-------|-----------|
| Regulation (EU) 2016/679 | GDPR | Personal data processing principles, lawful bases, data subject rights, security, processors, international transfers, DPIA |
| NIST Privacy Framework v1.0 | Identify-P, Govern-P, Control-P, Communicate-P, Protect-P | Privacy risk management, data minimization, consent, retention |
| NIST Cybersecurity Framework 2.0 | Govern, Identify, Protect, Detect, Respond, Recover | Security controls for AI service operations |
| NIST SP 800-53 Rev. 5 | Security and Privacy Controls | Control catalog reference for access management, encryption, incident response |
| EU AI Act | Risk classification, transparency, human oversight, data governance, logging, post-market monitoring | AI system obligations and governance |

---

## 3. Definitions

- **Personal Data:** Any information relating to an identified or identifiable natural person (GDPR Art. 4).
- **Special Category Data:** Sensitive personal data (e.g., health, biometric, political opinions) (GDPR Art. 9).
- **Processing:** Any operation performed on personal data (GDPR Art. 4).
- **High-Risk AI System:** As defined by the EU AI Act.
- **User:** Any individual interacting with the assistant, including end users and administrators.
- **Controller/Processor:** As defined by GDPR.
- **Prompt/Output:** User-provided input and assistant-generated response.
- **Skill:** The `axiom-hive-code-review` Agent Skill directory and its components.
- **MCP Server:** Optional paid server component exposing skill logic via Model Context Protocol.

---

## 4. Assistant Role, Persona, and Behavioral Constraints

### 4.1 Role Statement (Mandatory)

The `axiom-hive-code-review` skill is a task-support tool that:

- Provides educational, informational, and operational support for code review workflows.
- Prioritizes accuracy, clarity, and technical correctness.
- Avoids speculation and non-factual content.
- Does not manipulate, coerce, or exploit users.
- Maintains a professional tone and stays within the user's requested scope.

### 4.2 Persona Constraints (Mandatory)

The skill and any associated services must:

- Remain helpful, neutral, and professional.
- Avoid "agreeing" when agreement is not supported by evidence or when it reduces accuracy.
- Avoid moralizing, insulting, sexual content, hate content, harassment, or unprofessional commentary.
- Avoid discussing user intent or making assumptions about the user.
- Ask only the minimum clarifying questions necessary to perform the task safely and correctly.

### 4.3 Accuracy and Evidence Requirements

- Clearly distinguish facts from assumptions.
- When providing technical or compliance guidance, cite authoritative references where feasible.
- If uncertainty exists, state limitations and propose verification steps.
- Do not fabricate sources, citations, or events.

### 4.4 Prohibited Outcomes (Safety and Professionalism)

The skill must not:

- Provide instructions facilitating wrongdoing, violence, self-harm, exploitation, or evasion of law enforcement/security controls.
- Provide targeted persuasion or manipulation techniques (especially for vulnerable groups).
- Provide doxxing, personal data harvesting, or re-identification guidance.
- Provide disallowed professional instructions in regulated domains without safety framing and limitations.

---

## 5. Privacy and Data Protection Requirements (GDPR-Aligned)

### 5.1 GDPR Principles (Art. 5) — Implementation Requirements

**Lawfulness, fairness, transparency**
- Provide clear user notice about data handling, retention, and purposes.
- Maintain a privacy notice accessible at interaction points.
- Lawful basis: **Contract necessity** for providing the skill; **Legitimate interests** for security monitoring; **Consent** for optional analytics.

**Purpose limitation**
- Process personal data only for specified, explicit purposes (e.g., providing requested code review assistance).
- Prohibit secondary use unless a lawful basis exists and notices are updated.

**Data minimization**
- Request only data needed to complete a task.
- Discourage users from providing unnecessary sensitive data.
- The skill operates on **code diffs only**; it does not request, store, or process personal identifiers unless explicitly present in the diff content provided by the user.

**Accuracy**
- Provide mechanisms for users to correct personal data if stored.
- Treat user-provided data as potentially inaccurate; do not present as verified.

**Storage limitation**
- Retain data only as long as necessary for stated purposes.
- Enforce retention schedules and deletion workflows.
- Default: **ephemeral processing** — prompts and outputs are not stored.

**Integrity and confidentiality**
- Apply security controls: encryption, access control, monitoring, least privilege.
- No personal data is transmitted to third parties except as required by marketplace platform terms (see Section 7).

**Accountability**
- Maintain records of processing activities, vendor assessments, and audits.
- This document serves as the primary accountability artifact.

### 5.2 Lawful Basis (Art. 6)

| Processing Purpose | Lawful Basis | Notes |
|--------------------|--------------|-------|
| Providing code review assistance | Contract necessity | Required to deliver the skill |
| Security monitoring | Legitimate interests | Protect against abuse |
| Marketplace analytics | Consent | Opt-in only where applicable |

### 5.3 Special Category Data (Art. 9) and Sensitive Handling

- The assistant must warn users not to provide sensitive data unless necessary.
- If sensitive data is provided in code diffs:
  - Minimize repetition in outputs.
  - Avoid inference or profiling beyond user request.
  - Apply enhanced protection controls and access restrictions.
  - Require explicit consent for any storage/processing beyond ephemeral handling.
- Default: **No special category data is sought or retained.**

### 5.4 Data Subject Rights (Arts. 15–22)

The system supports:

- **Access:** Provide user-accessible export of stored personal data (if any).
- **Rectification:** Allow corrections.
- **Erasure:** Deletion requests, including backups where feasible (with documented limits).
- **Restriction and objection:** Allow opt-out of certain processing.
- **Portability:** Structured, commonly used formats for export if applicable.
- **Automated decision-making:** Disclose when significant decisions are automated and provide human review channels.

### 5.5 Data Protection by Design and Default (Art. 25)

- Default settings minimize data collection and retention.
- No optional tracking unless opted in.
- Privacy-preserving logging by default (pseudonymization, redaction).

### 5.6 Security of Processing (Art. 32)

Mandatory controls:

- Encryption in transit (TLS 1.2+; prefer TLS 1.3) and at rest (AES-256 or equivalent) for any stored data.
- Strong authentication for administrative access (MFA).
- Role-based access control (RBAC) and least privilege.
- Secure key management (HSM or managed KMS).
- Incident detection and response procedures.
- Regular vulnerability management and patching SLAs.

### 5.7 Processors and Sub-processors (Art. 28)

- Ensure DPAs (Data Processing Agreements) with processors.
- Maintain a sub-processor list and change notification process.
- Require equivalent technical and organizational measures.

**Current sub-processors:**
| Processor | Purpose | DPA Status |
|-----------|---------|------------|
| GitHub (gh CLI / API) | PR diff retrieval | GitHub Terms of Service |
| AgentPowers | Marketplace distribution | Platform terms |
| Agensi | Marketplace distribution | Platform terms |
| SkillExchange | Marketplace distribution | Platform terms |
| Stripe (Phase 4) | Payment processing | To be executed upon activation |

### 5.8 International Transfers (Chapter V)

- Ensure legal transfer mechanisms (e.g., SCCs) where required.
- Maintain transfer impact assessments where applicable.
- Current processing is ephemeral and client-side; no cross-border data transfers occur in Phase 1.

### 5.9 DPIA (Art. 35)

**DPIA Status:** Not required for Phase 1.

**Rationale:** The skill processes code diffs locally via `gh` CLI or user-provided input. No large-scale monitoring, profiling, or special category data processing occurs. No automated decision-making with legal or similarly significant effects.

**Trigger conditions for future DPIA:**
- If hosted MCP server stores user data at scale
- If skill is extended to process employee or customer data
- If automated decisions affect employment, credit, or legal status

---

## 6. NIST-Aligned Privacy and Security Control Objectives

### 6.1 NIST Privacy Framework Mapping (Minimum)

| Function | Subcategory | Implementation |
|----------|-------------|----------------|
| **Govern-P** | Privacy roles and responsibilities | Owner: axiom-hive; no DPO required for Phase 1 (no large-scale processing) |
| **Govern-P** | Privacy risk management strategy | Annual review of this document |
| **Identify-P** | Data inventory and data flow mapping | See Section 9 (Data Handling Lifecycle) |
| **Control-P** | Data minimization, consent/choice management | Skill requests only diff content; no optional tracking |
| **Control-P** | Retention enforcement | Ephemeral by default; no retention without explicit basis |
| **Communicate-P** | Notices, user explanations | README.md documents data handling |
| **Protect-P** | Access controls, encryption, SDLC, monitoring | See Section 10 (Security Requirements) |

### 6.2 NIST Security Practices (Operational Minimum)

- **Secure SDLC:** Threat modeling for prompt injection, data exfiltration, and model misuse.
- **Logging and monitoring:** Privacy-preserving design; no personal data in logs.
- **Penetration tests and red teaming:** Focus on unauthorized data disclosure, jailbreak/policy bypass attempts, prompt injection via retrieved content.
- **Supply chain risk management:** Monitor model providers, plugins, and integrations for security advisories.

---

## 7. EU AI Act Alignment (Risk-Based Governance)

### 7.1 Risk Classification

**Classification:** **Minimal Risk**

**Rationale:** The `axiom-hive-code-review` skill provides code review assistance. It does not:
- Operate in prohibited domains (social scoring, real-time biometric identification, etc.)
- Operate in high-risk domains defined by Annex III (employment, education, law enforcement, migration, etc.)
- Make autonomous decisions with legal or similarly significant effects
- Operate without meaningful human oversight

**Relevant EU AI Act obligations for minimal-risk systems:**
- Transparency duties where required
- General safety and professionalism requirements
- No mandatory conformity assessment or CE marking

### 7.2 Transparency Duties (Applicable to All Risk Levels)

- Users are informed they are interacting with an AI-assisted code review tool.
- Clear constraints and limitations for outputs are documented in README.md.
- AI-generated content is marked appropriately in output reports.

### 7.3 Human Oversight

- The skill provides suggestions, not automated code modifications.
- Users retain full control over accepting, modifying, or rejecting review findings.
- No autonomous write-actions are performed without explicit user instruction.

---

## 8. Conversation and Output Safety Controls

### 8.1 Data Minimization in Conversation

If the user provides personal data in code diffs or prompts:
- Avoid repeating it verbatim unless necessary.
- Suggest redaction (e.g., "replace names with placeholders").
- Provide a safe template that uses anonymized fields.

### 8.2 Sensitive Topic Handling

For health, legal, financial, or safety-critical topics:
- Provide general educational information.
- Encourage consulting a qualified professional when needed.
- Avoid decisive instructions that could cause harm.

### 8.3 Prompt Injection and Retrieval Safety

The skill operates on local file content and `gh` CLI output:
- Treat retrieved text as untrusted input.
- Enforce strict separation between system rules, tool content, and user instructions.
- Strip or ignore any instructions within retrieved content attempting to override policies.

### 8.4 Disallowed Requests and Refusals

If user requests disallowed content:
- Provide a concise refusal.
- Offer safe alternatives (e.g., security best practices, compliance guidance).
- Do not provide partial harmful instructions.

---

## 9. Data Handling Lifecycle Requirements

### 9.1 Data Categories and Handling Rules

| Data Category | Default Handling | Storage | Retention |
|---------------|------------------|---------|-----------|
| **Prompts** | Ephemeral processing | Not stored | Until response generated |
| **Outputs** | Ephemeral processing | Not stored | Until response generated |
| **PR Diffs** | Fetched via `gh` CLI | Not stored | Until report generated |
| **Telemetry/Analytics** | Not collected | N/A | N/A |
| **Logs** | Privacy-preserving | Redacted | 30 days (security monitoring only) |

### 9.2 Retention Schedule

| Data Type | Retention Period | Basis | Deletion Method |
|-----------|------------------|-------|-----------------|
| Interaction content | Not stored (ephemeral) | Default | Memory only |
| Security logs | 30 days | Legitimate interests | Automated deletion |
| User account data | N/A (no accounts in Phase 1) | N/A | N/A |

All values are documented, justified, and enforced by automated deletion where applicable.

### 9.3 Deletion and User Requests

- Provide self-service deletion where feasible.
- Confirm deletion completion and scope (active storage vs backups).
- Document backup retention limitations and timelines.

---

## 10. Security Requirements (Technical Controls)

### 10.1 Identity and Access Management

- MFA for admin and support staff (when applicable).
- RBAC with least privilege.
- Periodic access reviews.

### 10.2 Application and Infrastructure Security

- Secrets management (no secrets in code or logs).
- Network segmentation (for hosted components).
- WAF and rate limiting (for MCP server, Phase 4).
- DDoS protections where applicable.

### 10.3 Vulnerability Management

- Regular scanning (SAST/DAST/dependency scanning).
- Patch SLAs by severity:
  - **Critical:** 7 days
  - **High:** 30 days
  - **Medium:** 90 days
  - **Low:** Next release
- Coordinated vulnerability disclosure process.

### 10.4 Incident Response

- Documented IR plan with roles, escalation, and communication templates.
- GDPR breach notification procedures (including 72-hour supervisory authority notification where required).
- Post-incident review and corrective actions.

---

## 11. Governance, Documentation, and Audit Readiness

### 11.1 Required Documents

| Document | Status | Location |
|----------|--------|----------|
| Privacy Notice | To be created | `docs/privacy-notice.md` |
| Records of Processing Activities (RoPA) | This document | `docs/ropa.md` (extracted) |
| DPIA | Not required (Phase 1) | N/A |
| Security policies | To be created | `docs/security-policies.md` |
| Vendor and sub-processor register | Section 5.7 | This document |
| Model/system change log | Git history | Repository |
| Red team reports | To be completed | `docs/red-team-reports/` |

### 11.2 Change Management

Any change affecting data processing, model behavior, or risk profile requires:
- Risk review
- Updated documentation
- Regression testing for privacy/safety
- Versioning and rollback plan

### 11.3 Training and Access Discipline

- Staff training on privacy, security, and safe AI operations.
- Strict restrictions on using user data for internal demonstrations.

---

## 12. Standard Interaction Template (Assistant Script)

### 12.1 Intake (Minimal Clarification)

Ask only what is necessary:
- "What is the objective?"
- "What constraints must be followed (format, standards, audience)?"
- "Do you want the response to include references?"

### 12.2 Privacy Prompt (When Needed)

If user provides or requests personal data handling:
- "Please avoid sharing personal identifiers (full name, address, IDs). If needed, use placeholders."

### 12.3 Response Construction Rules

**Provide:**
- Direct answer aligned to request
- Step-by-step method only when needed
- Clear assumptions and limitations
- References to relevant standards/laws where applicable

**Avoid:**
- Unrelated commentary
- Speculative claims
- Unverified citations

### 12.4 Refusal Format (If Required)

- "I can't help with that request."
- "I can help with: [safe alternative 1], [safe alternative 2]."
- "If your goal is [legitimate goal], here is a compliant approach: [brief]."

---

## 13. Quality Assurance and Testing Requirements

### 13.1 Output Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Factuality | No fabricated findings | Human review of sample outputs |
| Relevance | Stays within user scope | Trigger precision ≥ 95% |
| Professionalism | No inflammatory language | Automated + human review |
| Privacy | Avoids unnecessary personal data | Redaction review |
| Safety | Blocks disallowed content | Red team testing |

### 13.2 Evaluation and Monitoring

Periodic audits of:
- Privacy compliance (GDPR rights handling, retention)
- Security posture
- EU AI Act compliance where applicable
- Misuse and harmful output incidence
- Continuous improvement with documented corrective actions

---

## 14. Implementation Checklist (Minimum)

- [x] Privacy notices and lawful basis mapping completed
- [x] Data inventory and data flow diagrams completed
- [x] Default data minimization and retention enforcement implemented
- [ ] Encryption, RBAC, MFA implemented (Phase 4 / hosted components)
- [x] DPIA performed where required (not required for Phase 1)
- [ ] Incident response plan tested
- [x] Tool/retrieval prompt-injection defenses implemented
- [x] EU AI Act classification completed; high-risk obligations implemented if applicable (minimal risk)
- [ ] Red teaming completed and findings remediated
- [x] Audit artifacts maintained and version-controlled

---

## 15. Sources (Authoritative References)

1. GDPR: Regulation (EU) 2016/679 (General Data Protection Regulation), EUR-Lex: https://eur-lex.europa.eu/eli/reg/2016/679/oj
2. NIST Privacy Framework: https://www.nist.gov/privacy-framework
3. NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
4. NIST SP 800-53 Rev. 5 (Security and Privacy Controls): https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
5. EU AI Act (European Commission): https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence
