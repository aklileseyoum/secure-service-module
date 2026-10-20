"""Tests for UserService."""

import pytest
from secure_service_module.exceptions import (
    InvalidPasswordError,
    UserAlreadyExistsError,
)
from secure_service_module.models import User


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


def test_register_short_password_raises(service, repo) -> None:
    """Attempting to register with short length password raises InvalidPasswordError."""
    with pytest.raises(InvalidPasswordError, match="at least 8"):
        service.create_user("aline", "Abc@123")
    repo.save_user.assert_not_called()


def test_register_no_capital_letters(service, repo) -> None:
    """Attempting to register with password with no capital letters raises Invalid Password Error."""
    with pytest.raises(InvalidPasswordError, match="at least one uppercase letter"):
        service.create_user("aline", "abcd@1234")
    repo.save_user.assert_not_called()


def test_register_no_digits(service, repo) -> None:
    """Attempting to register with password with no digits raises Invalid Password Error."""
    with pytest.raises(InvalidPasswordError, match="at least one digit"):
        service.create_user("aline", "Abcd@efgh")
    repo.save_user.assert_not_called()


def test_register_no_symbols(service, repo) -> None:
    """Attempting to register with password with no symbols raises Invalid Password Error."""
    with pytest.raises(InvalidPasswordError, match="at least one symbol"):
        service.create_user("aline", "Abcde1234")
    repo.save_user.assert_not_called()
