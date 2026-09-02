#!/usr/bin/env bash
set -euo pipefail

REPO="${1:-}"
PR_NUMBER="${2:-}"

if [[ -z "$REPO" || -z "$PR_NUMBER" ]]; then
  echo "Usage: $0 <owner/repo> <pr_number>" >&2
  exit 1
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "Error: gh CLI is required but not installed." >&2
  echo "Install: https://cli.github.com/" >&2
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "Error: gh is not authenticated. Run 'gh auth login' first." >&2
  exit 1
fi

if ! gh pr view "$REPO" "$PR_NUMBER" >/dev/null 2>&1; then
  echo "Error: PR #$PR_NUMBER not found in $REPO or rate limited." >&2
  exit 1
fi

gh pr diff "$REPO" "$PR_NUMBER"
