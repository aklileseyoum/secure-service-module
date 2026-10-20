from secure_service_module.interfaces import UserRepository
from secure_service_module.models import User


class InMemoryUserRepository(UserRepository):
    """The implementation of UserRepository Interface."""

    def __init__(self):
        self.users: dict[str, User] = {}

    def search_user(self, username):
        return self.users.get(username)

    def save_user(self, user):
        raise NotImplementedError
