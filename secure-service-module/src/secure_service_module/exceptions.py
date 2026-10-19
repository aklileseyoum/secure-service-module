"""Custom exceptions for the authentication service."""


class UserAlreadyExistsError(Exception):
    """Exception raised when a user already exists in the system."""

    def __init__(self, message="User already exists."):
        self.message = message
        super().__init__(self.message)


class UserNotFoundError(Exception):
    """Exception raised when a user is not found in the system."""

    def __init__(self, message="User not found."):
        self.message = message
        super().__init__(self.message)


class InvalidPasswordError(Exception):
    """Exception raised when the provided password is incorrect."""

    def __init__(self, message="Invalid username or password."):
        self.message = message
        super().__init__(self.message)
