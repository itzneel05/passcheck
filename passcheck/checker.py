"""Core password strength logic (no external dependencies)."""

from __future__ import annotations

from dataclasses import dataclass, field

# A short blocklist of very common passwords. Kept small on purpose so the
# package stays dependency-free; swap in the rockyou list for production use.
COMMON_PASSWORDS = {
    "password",
    "123456",
    "123456789",
    "qwerty",
    "abc123",
    "password1",
    "letmein",
    "iloveyou",
    "admin",
    "welcome",
    "monkey",
    "dragon",
}


@dataclass
class PasswordReport:
    """Structured result of checking a single password.

    Note: the plaintext password is deliberately NOT retained on this object.
    """

    score: int  # 0 (very weak) .. 4 (strong)
    label: str
    length: int
    guesses: int  # rough lower-bound of guesses to crack
    feedback: list[str] = field(default_factory=list)
    is_common: bool = False

    def as_dict(self) -> dict:
        return {
            "score": self.score,
            "label": self.label,
            "length": self.length,
            "guesses": self.guesses,
            "feedback": self.feedback,
            "is_common": self.is_common,
        }


def _pool_size(password: str) -> int:
    """Estimate the search space size based on character classes used."""
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(not c.isalnum() for c in password):
        pool += 33
    return pool or 1


def strength_label(score: int) -> str:
    return {0: "Very Weak", 1: "Weak", 2: "Fair", 3: "Good", 4: "Strong"}.get(
        score, "Very Weak"
    )


def check_password(password: str) -> PasswordReport:
    """Score a password from 0-4 and return actionable feedback."""
    feedback: list[str] = []
    length = len(password)
    is_common = password.lower() in COMMON_PASSWORDS

    # Character variety (0-3 points worth).
    variety = sum(
        [
            any(c.islower() for c in password),
            any(c.isupper() for c in password),
            any(c.isdigit() for c in password),
            any(not c.isalnum() for c in password),
        ]
    )

    # Rough lower-bound guesses: pool_size ^ length (capped to a big int).
    pool = _pool_size(password)
    try:
        guesses = min(pool**length, 10**15)
    except OverflowError:  # pragma: no cover - extremely long input
        guesses = 10**15

    # Base score is driven by length — the dominant factor in real strength.
    if length < 8:
        score = 0
    elif length < 12:
        score = 1
    else:
        score = 2

    # Variety bonus only counts once the password is long enough to benefit.
    # Without this guard a 4-character password could score "Good".
    if length >= 8:
        score = min(4, score + max(0, variety - 1))

    # Low-entropy shapes get capped: a single character class is weak, and a
    # digits-only password is brute-forced trivially no matter how long.
    if variety <= 1:
        score = min(score, 1)
    if password.isdigit():
        score = 0

    # Penalties and targeted advice.
    if is_common:
        score = 0
        feedback.append("This is a commonly used password — avoid it.")
    if length < 12:
        feedback.append("Use at least 12 characters.")
    if variety < 3:
        feedback.append("Mix upper case, lower case, digits, and symbols.")
    if password.isdigit():
        feedback.append("Numbers alone are easy to brute force.")
    if not feedback:
        feedback.append("Looks good — long and varied.")

    return PasswordReport(
        score=score,
        label=strength_label(score),
        length=length,
        guesses=guesses,
        feedback=feedback,
        is_common=is_common,
    )
