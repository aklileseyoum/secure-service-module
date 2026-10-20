from secure_service_module.exceptions import (
    InvalidPasswordError,
    UserAlreadyExistsError,
    UserNotFoundError,
)
from secure_service_module.interfaces import PasswordHasher, UserRepository
from secure_service_module.models import User


class UserService:
    def __init__(self, user_repo: UserRepository, pass_hash: PasswordHasher):
        self.user_repo = user_repo
        self.pass_hash = pass_hash

    def create_user(self, username: str, password: str) -> None:
        if self.user_repo.search_user(username) is not None:
            raise UserAlreadyExistsError("User with this username already exists.")
        self.password_check(password)
        password_hashed = self.pass_hash.password_hash(password)
        user = User(username=username, password_hash=password_hashed)
        self.user_repo.save_user(user)

    def password_check(self, password: str) -> None:
        capital = any(ch.isupper() for ch in password)
        has_digit = any(ch.isdigit() for ch in password)
        has_symbol = any(not ch.isalnum() for ch in password)
        if len(password) < 8:
            raise InvalidPasswordError("Password must be at least 8 characters long.")
        if not capital:
            raise InvalidPasswordError(
                "Password must contain at least one uppercase letter."
            )
        if not has_digit:
            raise InvalidPasswordError("Password must contain at least one digit.")
        if not has_symbol:
            raise InvalidPasswordError(
                "Password must contain at least one symbol, such as ! or @."
            )

    def login(self, username: str, password: str) -> User | None:
        if self.user_repo.search_user(username) is None:
            raise UserNotFoundError("User with this username does not exists.")
        user = self.user_repo.search_user(username)
        if user is not None:
            self.pass_hash.password_validator(user, password)
        return user
