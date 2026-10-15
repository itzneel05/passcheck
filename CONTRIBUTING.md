# Contributing to passcheck

Thanks for helping improve `passcheck`. This document explains how to set up,
what we expect from changes, and how collaboration works on this repository.

## Code of Conduct

Be respectful and constructive. Harassment, discrimination, and personal
attacks are not tolerated. Assume good intent and keep discussion focused on
the work.

## Getting Started

```bash
git clone https://github.com/itzneel05/passcheck.git
cd passcheck
python -m pip install -e ".[dev]"
pytest -q
```

Requirements: Python 3.9+ and `pip`. The project has **no runtime
dependencies** by design — please keep it that way.

## How Changes Land

`master` is protected. You cannot push to it directly.

1. **Open an issue** describing the bug or idea (or pick an existing one).
2. **Create a short-lived branch** off `master`:
   `feature/<short-description>`, `fix/<short-description>`,
   `docs/<short-description>`, or `chore/<short-description>`.
3. **Make focused commits** — one logical change each, in the conventional
   style (`feat:`, `fix:`, `docs:`, `test:`, `chore:`).
4. **Add or update tests** for any behavior change.
5. **Open a pull request** against `master`. Fill in the PR template.
6. **Review**: a code owner (see `.github/CODEOWNERS`) must approve, and CI
   must be green before merge.

Keep pull requests small (aim for ~100 lines). Large changes should be split.

## Coding Standards

- Pure Python standard library only — no new runtime dependencies without
  discussion in an issue first.
- Follow the existing structure: core logic in `checker.py`, presentation in
  `cli.py`.
- Never retain or log the plaintext password. `PasswordReport` intentionally
  does not store it.
- Run `pytest -q` before opening a PR; all tests must pass.

## Reporting Bugs

Use the bug report template. Include your Python version, the exact command
you ran, expected vs actual behaviour, and a minimal reproduction.

## Security

Do **not** open a public issue for security problems. See
[SECURITY.md](SECURITY.md) for the private reporting process.

## License

By contributing, you agree that your contributions are licensed under the
[MIT License](LICENSE).
