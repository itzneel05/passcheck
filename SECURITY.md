# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.x     | ✅        |

## Reporting a Vulnerability

Please **do not** report security vulnerabilities through public GitHub
issues, discussions, or pull requests.

Instead, report privately using GitHub's built-in
[private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability)
by visiting the **Security** tab of this repository and clicking
**Report a vulnerability**.

Please include:

- A description of the issue and its impact
- Steps to reproduce, or a proof-of-concept
- The affected version
- Any suggested fix, if you have one

## What to Expect

- **Acknowledgement** within 3 business days.
- **Assessment** and a severity classification within 10 business days.
- **Fix and disclosure**: we aim to ship a patch promptly and will credit
  reporters who wish to be named. Please give us a reasonable window to
  release a fix before public disclosure.

## Scope

`passcheck` runs entirely locally and makes no network calls. The main risks
are logic issues in strength scoring and any accidental retention of the
plaintext password. Reports about either are in scope and welcome.
