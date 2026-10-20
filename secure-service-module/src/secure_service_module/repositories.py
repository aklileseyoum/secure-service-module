from secure_service_module.interfaces import UserRepository
from secure_service_module.models import User


class InMemoryUserRepository(UserRepository):
    """The implementation of UserRepository Interface."""

    def __init__(self) -> None:
        self.users: dict[str, User] = {}

    def search_user(self, username: str) -> User | None:
        return self.users.get(username)

    def save_user(self, user: User) -> None:
        self.users[user.username] = user
