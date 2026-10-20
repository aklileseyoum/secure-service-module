import pytest
from secure_service_module.exceptions import InvalidPasswordError, UserNotFoundError
from secure_service_module.models import User


def test_good_login(service, hasher, repo) -> None:
    repo.search_user.return_value = User(username="aline", password_hash="x")
    hasher.password_validator.return_value = True
    result = service.login("aline", "Secret123!")
    assert result.username == "aline"
    hasher.password_validator.assert_called_once_with(result, "Secret123!")


def test_user_doesnt_exist_login(service, hasher, repo) -> None:
    with pytest.raises(UserNotFoundError):
        service.login("aline", "Secret123!")
    hasher.password_validator.assert_not_called()


def test_incorrect_password_login(service, hasher, repo) -> None:
    user = User(username="aline", password_hash="x")
    repo.search_user.return_value = user
    hasher.password_validator.return_value = False
    with pytest.raises(InvalidPasswordError):
        service.login("aline", "Secret123!")
    hasher.password_validator.assert_called_once_with(user, "Secret123!")
