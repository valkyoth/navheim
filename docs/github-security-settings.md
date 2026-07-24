# GitHub Security Settings

Repository maintainers should enable:

- private vulnerability reporting;
- Dependabot alerts and security updates;
- secret scanning and push protection where available;
- branch protection with required Rust CI;
- CodeQL analysis default setup.

CodeQL analysis default setup is active by repository policy. Do not commit an
advanced CodeQL workflow while default setup is enabled.

Review workflow permissions, action SHA pins, dependency update status, and
security alerts before every release. Platform/security settings are external
state and must be recorded in release evidence rather than assumed from files.
