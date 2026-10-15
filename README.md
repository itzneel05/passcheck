# passcheck 🔐

A tiny, **dependency-free** command-line password strength checker written in pure Python.

It scores a password from 0–4 and gives actionable feedback — no network calls, no external libraries, nothing leaves your machine.

## Features

- **Zero dependencies** — pure Python standard library.
- **Honest scoring** — length, character variety, and a small common-password blocklist.
- **Rough crack-time estimate** — lower-bounds the guess space from the character pool.
- **Actionable feedback** — tells you *how* to improve, not just a grade.
- **Secure prompt** — omit the password argument to type it hidden.

## Install

```bash
pip install -e .
```

Or run it straight from the repo without installing:

```bash
python -m passcheck "your password"
```

## Usage

```bash
# Pass the password as an argument
passcheck "Sup3r$ecret-2026!"

# Or be prompted securely (input hidden)
passcheck

# Plain output for scripts / CI
passcheck --no-color "correct-horse-battery-staple-9"
```

### Example output

```
Strength : Strong
Score    : ████████████████████ 4/4
Length   : 19 chars
Feedback :
  - Looks good — long and varied.
```

## Scoring

| Score | Label      | Meaning                                   |
|------:|------------|-------------------------------------------|
|     0 | Very Weak  | Too short, common, or single character class |
|     1 | Weak       | Short or low variety                      |
|     2 | Fair       | Decent length, could be more varied       |
|     3 | Good       | Long and varied                           |
|     4 | Strong     | Long, varied, and not commonly used       |

## Development

```bash
pip install -e ".[dev]"
pytest
```

## License

MIT — see [LICENSE](LICENSE).
