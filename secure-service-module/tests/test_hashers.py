from secure_service_module.hashers import BcryptPasswordHasher


def test_hashing_password():
    hasher = BcryptPasswordHasher()
    hashed_password = hasher.password_hash("Secret123!")
    assert isinstance(hashed_password, str)
    assert hashed_password != "Secret123!"
