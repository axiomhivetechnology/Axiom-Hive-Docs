# Implementation Baseline

The first implementation slice is a model-independent policy boundary for a local-first image-text editor.

## Current scope

- Restricted document categories are redirected to redaction-only workflows.
- Deceptive intent is refused.
- Missing image category or purpose does not default to permission.
- Cloud processing, diagnostics, analytics, project storage, and training use default to opt-in.
- Metadata scrubbing and optional provenance defaults are privacy-first.

OCR, inpainting, style matching, and export codecs must call this boundary before processing user content. They are intentionally not implemented in this slice.

## Run tests

```sh
PYTHONPATH=src python3 -m unittest discover -s tests
```
