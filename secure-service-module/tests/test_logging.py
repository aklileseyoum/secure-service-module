import logging

import pytest
from secure_service_module.exceptions import UserAlreadyExistsError
from secure_service_module.models import User


def test_registeration_succeeds(service, caplog):
    caplog.set_level(logging.INFO)
    service.create_user("aline", "Secret123!")
    assert "aline" in caplog.text
    assert "Secret123!" not in caplog.text


def test_registration_rejected_logged(service, repo, caplog):
    caplog.set_level(logging.INFO)
    repo.search_user.return_value = User(username="aline", password_hash="x")
    with pytest.raises(UserAlreadyExistsError):
        service.create_user("aline", "Secret123!")
    assert "aline" in caplog.text
    assert "Secret123!" not in caplog.text
