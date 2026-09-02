---
name: axiom-hive-code-review
description: Performs structured code review on GitHub pull request diffs. Returns severity-scored findings (security, performance, style, logic) with confidence levels and suggested fixes. Use when asked to review a PR, analyze a pull request, or check code changes on GitHub.
license: MIT
compatibility: Requires gh CLI (authenticated) and Python 3.10+
metadata:
  version: "1.0.0"
  author: axiom-hive
  repository: https://github.com/axiom-hive/axiom-hive-code-review
---

# GitHub PR Diff Analyzer

Review a GitHub pull request by fetching its diff, analyzing changes against a severity rubric, and returning a structured Markdown report with actionable findings.

## Workflow

1. Confirm the target repository and PR number.
2. Fetch the PR diff using `scripts/analyze-pr.sh`.
3. Feed the diff into `scripts/generate-report.py`.
4. Format the output using `assets/review-template.md`.
5. Apply scoring rules from `assets/severity-rubric.json` and reference guidance from `references/best-practices.md` and `references/error-catalog.md`.
6. Return the final Markdown review to the user.

## Inputs

- `repo`: GitHub repository in `owner/repo` format.
- `pr_number`: Positive integer PR number.

## Output

Markdown review containing:
- PR metadata
- Summary paragraph
- Findings grouped by severity
- Suggested fixes
- Overall assessment

## Edge Cases

- Empty diff: report "No changes to review."
- Binary files: note presence, skip diff analysis.
- Merge conflicts: flag as `major` and stop automated analysis.
- Large PRs (>300 files): summarize top risk areas instead of line-by-line findings.

## References

- `references/best-practices.md` — review criteria and checklists
- `references/error-catalog.md` — common bug patterns
- `assets/severity-rubric.json` — scoring rules
- `assets/review-template.md` — output template
