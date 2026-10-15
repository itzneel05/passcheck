"""Tests for the command-line interface."""

import json

from passcheck.cli import main


def test_json_output(capsys):
    assert main(["--json", "correct-horse-battery-staple-9"]) == 0

    output = capsys.readouterr().out
    assert json.loads(output) == {
        "score": 4,
        "label": "Strong",
        "length": 30,
        "guesses": 10**15,
        "feedback": ["Looks good — long and varied."],
        "is_common": False,
    }
