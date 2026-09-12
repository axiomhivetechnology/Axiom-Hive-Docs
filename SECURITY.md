# Security Policy

## Scope

This repository contains documentation and an early policy prototype. It is not a hosted service and should not be used as the sole control for high-risk or consequential decisions.

## Reporting A Vulnerability

Please do not open a public issue for a suspected vulnerability or include secrets, personal data, credentials, or private image content in a report.

Use the repository owner's private GitHub security reporting channel when available. If that channel is unavailable, contact the maintainers privately through the organization associated with this repository and include:

- a concise description of the issue;
- affected file or component;
- reproducible steps using synthetic data only;
- potential impact;
- a suggested mitigation, if known.

Allow maintainers reasonable time to investigate before public disclosure. Never test against systems or data that you do not own or have explicit permission to assess.

## Security Expectations

Contributors should avoid committing credentials, user data, model artifacts containing personal information, or logs with sensitive content. Future processing components should include sandboxing, least privilege, dependency review, secure deletion, and explicit retention controls.
