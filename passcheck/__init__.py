"""passcheck - a tiny, dependency-free password strength checker."""

from .checker import PasswordReport, check_password, strength_label

__all__ = ["PasswordReport", "check_password", "strength_label"]
__version__ = "1.0.0"
