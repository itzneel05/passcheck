"""Command-line interface for passcheck."""

from __future__ import annotations

import argparse
import getpass
import sys

from .checker import check_password

# ANSI colours, disabled automatically when piped or on no-TTY.
_COLORS = {"0": "\033[31m", "1": "\033[31m", "2": "\033[33m", "3": "\033[36m", "4": "\033[32m"}
_RESET = "\033[0m"


def _paint(text: str, score: int, use_color: bool) -> str:
    if not use_color:
        return text
    return f"{_COLORS.get(str(score), '')}{text}{_RESET}"


def _bar(score: int) -> str:
    return "█" * (score + 1) + "░" * (4 - score)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="passcheck",
        description="Check the strength of a password.",
    )
    parser.add_argument(
        "password",
        nargs="?",
        help="Password to check (omit to be prompted securely).",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable coloured output.",
    )
    args = parser.parse_args(argv)

    use_color = not args.no_color and sys.stdout.isatty()

    if args.password is not None:
        password = args.password
    else:
        try:
            password = getpass.getpass("Password: ")
        except (EOFError, KeyboardInterrupt):
            print("\nAborted.")
            return 1

    report = check_password(password)

    print(f"Strength : {_paint(report.label, report.score, use_color)}")
    print(f"Score    : {_paint(_bar(report.score), report.score, use_color)} {report.score}/4")
    print(f"Length   : {report.length} chars")
    print("Feedback :")
    for line in report.feedback:
        print(f"  - {line}")

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
