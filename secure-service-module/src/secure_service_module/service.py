from secure_service_module.exceptions import (
    InvalidPasswordError,
    UserAlreadyExistsError,
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
        if len(password) < 8:
            raise InvalidPasswordError("Password must be at least 8 characters long.")
