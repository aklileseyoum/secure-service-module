"""Tests for UserService."""

import pytest
from pytest_mock import MockerFixture
from secure_service_module.exceptions import UserAlreadyExistsError
from secure_service_module.interfaces import PasswordHasher, UserRepository
from secure_service_module.models import User
from secure_service_module.service import UserService


@pytest.fixture
def repo(mocker: MockerFixture):
    """A fake repository where no user exists yet."""
    fake = mocker.create_autospec(UserRepository, instance=True)
    fake.search_user.return_value = None
    return fake


@pytest.fixture
def hasher(mocker: MockerFixture):
    """A fake hasher that returns a recognisable hash."""
    fake = mocker.create_autospec(PasswordHasher, instance=True)
    fake.password_hash.return_value = "hashed-value"
    return fake


@pytest.fixture
def service(repo, hasher) -> UserService:
    """A UserService wired to the fakes."""
    return UserService(repo, hasher)


def test_register_saves_user_with_hash(service, repo) -> None:
    """Registering a new user saves them with a hash, not the plain password."""
    service.create_user("aline", "Secret123!")
    repo.save_user.assert_called_once()
    saved = repo.save_user.call_args.args[0]
    assert saved.username == "aline"
    assert saved.password_hash == "hashed-value"


def test_register_duplicate_username_raises(service, repo) -> None:
    """Registering a taken username raises UserAlreadyExistsError."""
    repo.search_user.return_value = User(username="aline", password_hash="x")
    with pytest.raises(UserAlreadyExistsError):
        service.create_user("aline", "Secret123!")
    repo.save_user.assert_not_called()
