from secure_service_module.models import User


def test_good_login(service, hasher, repo) -> None:
    repo.search_user.return_value = User(username="aline", password_hash="x")
    hasher.password_validator.return_value = True
    result = service.login("aline", "Secret123!")
    assert result.username == "aline"
    hasher.password_validator.assert_called_once_with("Secret123!", "x")
