import bcrypt

from secure_service_module.interfaces import PasswordHasher
from secure_service_module.models import User


class BcryptPasswordHasher(PasswordHasher):
    """Implementation of the interface PasswordHasher"""

    def password_hash(self, password: str) -> str:
        """Hashes the given password.
        Args:
            password: the password to be hashed.

        Result:
            password_hashed: the hashed password.
        """
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed.decode("utf-8")

    def password_validator(self, user: User, password_unhashed: str) -> bool:
        """checks if the password is correct.
        Args:
            user: user object that holds username and hashed password
            password_unhashed: the password from user's input

        Return:
            True: if the password matches.
            False: if the password doesn't match.
        """
        return bcrypt.checkpw(
            password_unhashed.encode("utf-8"), user.password_hash.encode("utf-8")
        )
