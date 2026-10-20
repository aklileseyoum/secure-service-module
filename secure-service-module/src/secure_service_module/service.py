from secure_service_module.interfaces import PasswordHasher, UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository, pass_hash: PasswordHasher):
        self.user_repo = user_repo
        self.pass_hash = pass_hash

    def create_user(self, username: str, password: str) -> None:
        raise NotImplementedError

    def password_check(self, password: str) -> None:
        raise NotImplementedError
