"""Tests for the core password checker logic."""

from passcheck.checker import check_password, strength_label


def test_empty_is_very_weak():
    r = check_password("")
    assert r.score == 0
    assert r.label == "Very Weak"


def test_common_password_is_flagged():
    r = check_password("password")
    assert r.is_common is True
    assert r.score == 0
    assert any("commonly used" in f for f in r.feedback)


def test_long_varied_password_is_strong():
    r = check_password("Sup3r$ecret-2026!")
    assert r.score == 4
    assert r.label == "Strong"


def test_digits_only_is_weak():
    r = check_password("123456789012")
    assert r.score <= 1
    assert any("Numbers alone" in f for f in r.feedback)


def test_short_password_penalised():
    r = check_password("Ab1!")
    assert r.score == 0
    assert any("12 characters" in f for f in r.feedback)


def test_feedback_present_when_good():
    r = check_password("correct-horse-battery-staple-9")
    assert r.feedback  # non-empty
    assert r.score >= 3


def test_strength_label_mapping():
    assert strength_label(0) == "Very Weak"
    assert strength_label(4) == "Strong"
    assert strength_label(99) == "Very Weak"  # out of range falls back


def test_as_dict_shape():
    d = check_password("passw0rd!").as_dict()
    assert set(d) == {"score", "label", "length", "guesses", "feedback", "is_common"}
