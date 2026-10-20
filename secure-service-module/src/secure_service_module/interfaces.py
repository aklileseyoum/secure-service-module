"""Stores users and Hashes Passwords."""

from abc import ABC, abstractmethod

from secure_service_module.models import User


class UserRepository(ABC):
    """Interface to store users."""

    @abstractmethod
    def search_user(self, username: str) -> User | None:
        """Searches if user exists.
        Args:
            user: The user whom we are searching
        Return:
            User: if the user is found.
            None: if the user is not found
        """

    @abstractmethod
    def save_user(self, user: User) -> None:
        """Saves the user.
        Args:
            user: The user to be saved.
        """


class PasswordHasher(ABC):
    """Interface to hash the passwords"""

    @abstractmethod
    def password_hash(self, password: str) -> str:
        """Hashes the given password.
        Args:
            password: the password to be hashed.

        Result:
            password_hashed: the hashed password.
        """

    @abstractmethod
    def password_validator(self, password: str, hashed: str) -> bool:
        """checks if the password is correct.
        Args:
            hashed: the hashed value of a potential password
            password: the password from user's input

        Return:
            True: if the password matches.
            False: if the password doesn't match.
        """
