#!/usr/bin/env python3
import sys
import json
import re
from pathlib import Path

RUBRIC_PATH = Path(__file__).resolve().parent.parent / "assets" / "severity-rubric.json"

def load_rubric():
    with open(RUBRIC_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def filter_diff_content(diff_text: str) -> str:
    lines = diff_text.splitlines()
    content_lines = []
    for line in lines:
        stripped = line.rstrip("\n")
        if stripped.startswith("+") and not stripped.startswith("+++"):
            content_lines.append(stripped[1:])
        elif stripped.startswith(" ") and not stripped.startswith("--- "):
            content_lines.append(stripped[1:])
    return "\n".join(content_lines)

def score_diff(diff_text: str, rubric: dict) -> list:
    findings = []
    content = filter_diff_content(diff_text)
    patterns = rubric.get("patterns", [])
    for entry in patterns:
        pattern = entry.get("pattern", "")
        severity = entry.get("severity", "info")
        confidence = entry.get("confidence", "medium")
        category = entry.get("category", "general")
        message = entry.get("message", "")
        fix = entry.get("fix", "")
        if re.search(pattern, content, re.IGNORECASE):
            findings.append({
                "severity": severity,
                "confidence": confidence,
                "category": category,
                "message": message,
                "fix": fix,
            })
    return findings

def group_by_severity(findings: list) -> dict:
    order = ["critical", "major", "minor", "info", "suggestion"]
    grouped = {k: [] for k in order}
    for finding in findings:
        sev = finding.get("severity", "info")
        if sev in grouped:
            grouped[sev].append(finding)
    return {k: v for k, v in grouped.items() if v}

def render_report(repo: str, pr_number: str, diff_text: str) -> str:
    rubric = load_rubric()
    findings = score_diff(diff_text, rubric)
    grouped = group_by_severity(findings)
    changed_files = len(re.findall(r"^\+\+\+ ", diff_text, re.MULTILINE))

    lines = []
    lines.append(f"# PR Review: {repo} #{pr_number}")
    lines.append("")
    lines.append(f"**Files changed:** {changed_files}")
    lines.append("")

    if not findings:
        lines.append("## Summary")
        lines.append("")
        lines.append("No issues matched the configured rubric. Review manually for business logic and design.")
        lines.append("")
        return "\n".join(lines)

    lines.append("## Summary")
    lines.append("")
    lines.append(f"Found {len(findings)} issue(s) across {len(grouped)} severity level(s). Review the findings below and address critical and major items before merge.")
    lines.append("")

    for severity in ["critical", "major", "minor", "info", "suggestion"]:
        items = grouped.get(severity)
        if not items:
            continue
        lines.append(f"## {severity.title()}")
        lines.append("")
        for item in items:
            lines.append(f"- **{item['message']}** (confidence: {item['confidence']})")
            if item.get("fix"):
                lines.append(f"  - Fix: {item['fix']}")
        lines.append("")

    lines.append("## Suggested Fixes")
    lines.append("")
    for severity in ["critical", "major"]:
        items = grouped.get(severity, [])
        for item in items:
            if item.get("fix"):
                lines.append(f"1. {item['fix']}")
    lines.append("")

    overall = "Request Changes" if grouped.get("critical") or grouped.get("major") else "Comment"
    lines.append(f"**Overall:** {overall}")
    lines.append("")
    return "\n".join(lines)

def main():
    if len(sys.argv) < 2:
        print("Usage: generate-report.py <diff_file> [repo owner/repo] [pr_number]", file=sys.stderr)
        sys.exit(1)

    diff_path = Path(sys.argv[1])
    repo = sys.argv[2] if len(sys.argv) > 2 else "unknown/unknown"
    pr_number = sys.argv[3] if len(sys.argv) > 3 else "0"

    diff_text = diff_path.read_text(encoding="utf-8", errors="replace")
    report = render_report(repo, pr_number, diff_text)
    print(report)

if __name__ == "__main__":
    main()
