# Axiom Hive Docs

Safety-first documentation and implementation foundations for privacy-preserving AI image and text editing workflows.

This repository contains two related layers:

1. **A policy boundary prototype** in `src/axiom_image_editing/` that makes a conservative allow, redact-only, or refuse decision before an image-editing pipeline runs.
2. **The `axiom-hive-code-review` agent skill** in `Artifical Intel. Docs/Docs/Ai Agent Skiills:Logic/` for structured GitHub pull-request reviews with severity scoring, privacy guidance, and machine-readable output support.

The repository is intentionally honest about its maturity: the policy module is a tested foundation, not a complete image editor, and the agent skill is documentation plus supporting scripts rather than a hosted service.

## What Is Included

### Policy foundation

The Python module currently provides:

- explicit handling for restricted document categories;
- refusal of deceptive editing purposes;
- conservative behavior when image category or purpose is missing;
- opt-in settings for cloud processing, diagnostics, analytics, project storage, and training use;
- privacy-first export defaults that scrub metadata and keep provenance optional.

OCR, inpainting, style matching, codecs, and a user interface are outside the current implementation scope. Any future processing pipeline should call `evaluate_edit` before handling user content.

### Code-review agent skill

The skill analyzes GitHub pull-request diffs and produces structured Markdown reviews with:

- findings grouped by severity;
- confidence levels and suggested fixes;
- deterministic safety and privacy rules;
- optional JSON Schema validation;
- references covering review practice, compliance, and refusal handling.

See the [skill guide](Artifical%20Intel.%20Docs/Docs/Ai%20Agent%20Skiills%3ALogic/axiom-hive-code-review/README.md) for installation and usage.

## Repository Layout

```text
src/axiom_image_editing/       Policy boundary prototype
tests/                          Unit tests for policy behavior
Artifical Intel. Docs/          Agent skill, safety, and compliance documentation
IMPLEMENTATION.md               Current scope and implementation status
CONTRIBUTING.md                 Contribution workflow and quality checks
SECURITY.md                     Responsible security reporting guidance
```

## Quick Start

Requirements: Python 3.10 or newer.

Run the test suite from the repository root:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

Try the policy boundary directly:

```bash
PYTHONPATH=src python3 -c \
 'from axiom_image_editing.policy import evaluate_edit; print(evaluate_edit("poster", "replace fictional title"))'
```

Expected result:

```text
EditDecision.ALLOW
```

## Safety And Privacy Position

- Legitimate creative editing should require a stated image category and purpose.
- Official documents, credentials, financial records, medical records, and similar materials are redirected to redaction-only workflows.
- Requests indicating fraud, impersonation, bypassing verification, or counterfeit creation are refused.
- Local processing is the default design goal; cloud inference, analytics, diagnostics, storage, and training use require separate opt-in consent.
- Export should scrub unnecessary metadata by default while allowing users to preserve selected technical metadata.
- AI assistance, limitations, provenance behavior, retention, and deletion controls should be disclosed clearly in any product built on this foundation.

These controls reduce risk but do not make an edited image authentic, lawful, or suitable for a consequential decision. Human review remains required.

## Project Status

This is an early, model-independent foundation. The current release is useful for policy evaluation and documentation review, but it does not yet provide a production image-editing application, model serving, persistence, authentication, or a web API.

Planned work is tracked in [IMPLEMENTATION.md](IMPLEMENTATION.md). Contributions should preserve the conservative defaults and add tests for every new policy branch.

## License

Released under the [MIT License](LICENSE).
