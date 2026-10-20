from secure_service_module.hashers import BcryptPasswordHasher
from secure_service_module.models import User


def test_hashing_password():
    hasher = BcryptPasswordHasher()
    hashed_password = hasher.password_hash("Secret123!")
    assert isinstance(hashed_password, str)
    assert hashed_password != "Secret123!"


def test_password_validator():
    hasher = BcryptPasswordHasher()
    user = User(username="aline", password_hash=hasher.password_hash("Secret123!"))
    assert hasher.password_validator(user, "Secret123!")
