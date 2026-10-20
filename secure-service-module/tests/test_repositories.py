from secure_service_module.repositories import InMemoryUserRepository


def test_search_user_from_empty() -> None:
    repo = InMemoryUserRepository()
    assert repo.search_user("aline") is None
