# Axiom Hive Code Review

Structured GitHub PR code review skill for Claude Code, Cursor, and Codex CLI.

## What It Does

Fetches a GitHub pull request diff, analyzes changes against a severity rubric, and returns a Markdown review with:

- Severity-scored findings (critical, major, minor, info, suggestion)
- Confidence levels for each finding
- Suggested fixes
- Overall assessment

## Prerequisites

- `gh` CLI installed and authenticated
- Python 3.10 or higher
- Git repository with GitHub remote

## Installation

### Claude Code

```bash
cp -r axiom-hive-code-review ~/.claude/skills/
```

### Cursor

Copy the `axiom-hive-code-review` folder into your Cursor rules or skills directory.

### Codex CLI

Copy the folder into your project's `.agents/skills/` directory.

## Usage

Ask your AI assistant:

```
Review PR 42 in owner/repo
```

Or:

```
Analyze the diff for pull request #123 in octocat/Hello-World
```

The skill will:
1. Fetch the PR diff via `gh pr diff`
2. Analyze changes against the severity rubric
3. Return a structured Markdown report

## Customization

### Extend the Error Catalog

Edit `references/error-catalog.md` to add domain-specific patterns.

### Adjust the Rubric

Modify `assets/severity-rubric.json` to change severity rules or add new patterns.

### Change Output Format

Edit `assets/review-template.md` to restructure the report.

## Troubleshooting

**`gh` is not authenticated**
Run `gh auth login` and follow the prompts.

**Rate limited**
GitHub API rate limits apply. Use `GITHUB_TOKEN` environment variable for higher limits.

**Large PRs**
PRs with >300 files are summarized automatically. Adjust the threshold in `scripts/generate-report.py`.

## License

MIT
