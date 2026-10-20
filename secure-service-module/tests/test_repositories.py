from secure_service_module.models import User
from secure_service_module.repositories import InMemoryUserRepository


def test_search_user_from_empty() -> None:
    repo = InMemoryUserRepository()
    assert repo.search_user("aline") is None


def test_search_user_from_list() -> None:
    repo = InMemoryUserRepository()
    repo.save_user(User(username="aline", password_hash="x"))
    assert repo.search_user("aline") is not None
