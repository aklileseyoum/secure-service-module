import logging

import pytest
from secure_service_module.exceptions import (
    InvalidPasswordError,
    UserAlreadyExistsError,
)
from secure_service_module.models import User


def test_registeration_succeeds(service, caplog) -> None:
    caplog.set_level(logging.INFO)
    service.create_user("aline", "Secret123!")
    assert "aline" in caplog.text
    assert "Secret123!" not in caplog.text


def test_registration_rejected_logged(service, repo, caplog) -> None:
    caplog.set_level(logging.WARNING)
    repo.search_user.return_value = User(username="aline", password_hash="x")
    with pytest.raises(UserAlreadyExistsError):
        service.create_user("aline", "Secret123!")
    assert "aline" in caplog.text
    assert "Secret123!" not in caplog.text


def test_login_succeed(service, repo, hasher, caplog) -> None:
    caplog.set_level(logging.INFO)
    repo.search_user.return_value = User(username="aline", password_hash="x")
    hasher.password_validator.return_value = True
    service.login("aline", "Secret123!")
    assert "aline" in caplog.text
    assert "Secret123!" not in caplog.text


def test_login_failed(service, repo, hasher, caplog) -> None:
    caplog.set_level(logging.WARNING)
    repo.search_user.return_value = User(username="aline", password_hash="x")
    hasher.password_validator.return_value = False
    with pytest.raises(InvalidPasswordError):
        service.login("aline", "Wrong123!")
    assert "aline" in caplog.text
    assert "Wrong123!" not in caplog.text
