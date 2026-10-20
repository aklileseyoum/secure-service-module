"""Data model for Users"""

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    """A user record saved from registeration.

    Attributes:
        username: The user's username.
        password_hash: The hashed value of the user's password.
    """

    username: str
    password_hash: str
