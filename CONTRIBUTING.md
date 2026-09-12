# Contributing

Thank you for helping improve Axiom Hive Docs. Keep changes focused, evidence-based, and consistent with the repository's privacy-first goals.

## Before Opening A Pull Request

1. Read [IMPLEMENTATION.md](IMPLEMENTATION.md) and the relevant documentation under `Artifical Intel. Docs/`.
2. Keep public APIs and conservative policy defaults stable unless the change explicitly requires an update.
3. Add or update tests for changed behavior.
4. Run the test suite:

   ```bash
   PYTHONPATH=src python3 -m unittest discover -s tests
   ```

5. Review the diff for secrets, personal data, generated artifacts, and unrelated formatting changes.

## Policy Changes

Policy changes need clear reasoning and focused test cases. Do not weaken a refusal or redaction boundary without documenting the intended use case, the risk considered, and the safer alternative for ambiguous input.

## Documentation Changes

Use plain language, distinguish verified behavior from planned behavior, and avoid presenting regulatory alignment as legal advice or a guarantee.

## Pull Requests

Describe the problem, the change, the tests run, and any remaining limitations. Small pull requests are easier to review and safer to merge.
