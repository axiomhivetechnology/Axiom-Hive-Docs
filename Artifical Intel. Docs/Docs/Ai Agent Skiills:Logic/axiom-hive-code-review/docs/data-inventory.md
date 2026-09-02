# Data Inventory and Data Flow

**Document ID:** AXIOM-DATA-001  
**Effective Date:** 2026-09-02  
**Product:** axiom-hive-code-review

---

## Data Categories

### 1. Prompts (User Input)
- **Description:** User requests to review a PR, analyze changes, or check code.
- **Format:** Natural language text.
- **Sensitivity:** May contain code diffs with incidental personal data.
- **Handling:** Ephemeral; processed in context only, not stored.

### 2. PR Diffs (Tool Output)
- **Description:** Output from `gh pr diff` or GitHub API.
- **Format:** Unified diff text.
- **Sensitivity:** May contain code, comments, and incidental personal data.
- **Handling:** Ephemeral; passed to analysis scripts, not stored.

### 3. Review Reports (Generated Output)
- **Description:** Structured Markdown review with findings.
- **Format:** Markdown text.
- **Sensitivity:** May repeat code snippets and incidental personal data from diffs.
- **Handling:** Ephemeral; returned to user, not stored.

### 4. GitHub Authentication Tokens
- **Description:** `gh` CLI authentication state or `GITHUB_TOKEN` environment variable.
- **Format:** OAuth token or personal access token.
- **Sensitivity:** High (credentials).
- **Handling:** Managed locally by user or environment; never logged or transmitted by the skill.

### 5. Marketplace Analytics (Optional, Future)
- **Description:** Aggregated usage metrics, sales data.
- **Format:** Aggregated statistics.
- **Sensitivity:** Low (anonymized).
- **Handling:** Processed by marketplace platforms under their respective privacy policies.

---

## Data Flow Diagram

```
User Request
    │
    ▼
[Claude Code / Cursor / Codex]
    │
    ├──▶ SKILL.md (instructions)
    │
    ▼
[scripts/analyze-pr.sh]
    │
    ├──▶ gh CLI (authenticated)
    │       │
    │       ▼
    │   [GitHub API]
    │       │
    │       ▼
    │   PR Diff (unified format)
    │
    ▼
[scripts/generate-report.py]
    │
    ├──▶ assets/severity-rubric.json
    ├──▶ references/best-practices.md
    ├──▶ references/error-catalog.md
    │
    ▼
Structured Markdown Report
    │
    ▼
User (displayed in chat)
```

**Key privacy controls:**
- No persistent storage of prompts, diffs, or reports
- No external transmission of data except GitHub API calls initiated by `gh` CLI
- User controls GitHub authentication locally

---

## Data Retention

| Data Type | Retention Period | Deletion Method |
|-----------|------------------|-----------------|
| Prompts | Ephemeral (session only) | Memory / context window |
| PR Diffs | Ephemeral (processing only) | Memory / temp files |
| Review Reports | Ephemeral (session only) | Memory / context window |
| GitHub Tokens | User-managed | User-controlled |
| Logs | 30 days max | Automated deletion |
