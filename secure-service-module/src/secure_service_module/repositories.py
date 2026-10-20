from secure_service_module.interfaces import UserRepository
from secure_service_module.models import User


class InMemoryUserRepository(UserRepository):
    """The implementation of UserRepository Interface."""

    def __init__(self) -> None:
        self.users: dict[str, User] = {}

    def search_user(self, username: str) -> User | None:
        """Searches if user exists.
        Args:
            user: The user whom we are searching
        Return:
            User: if the user is found.
            None: if the user is not found
        """
        return self.users.get(username)

    def save_user(self, user: User) -> None:
        """Saves the user.
        Args:
            user: The user to be saved.
        """
        self.users[user.username] = user
