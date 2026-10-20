"""Stores components for the test files."""

import pytest
from pytest_mock import MockerFixture
from secure_service_module.interfaces import PasswordHasher, UserRepository
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
