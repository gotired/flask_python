"""Custom Error for app"""


class CustomError(Exception):
    """Custom error"""

    def __init__(self, message, status_code=400, location=None):
        super().__init__(message)
        self.status_code = status_code
        self.location = location


class InsertError(CustomError):
    """Insert document error"""

    def __init__(self, message="Insert document error", location=None):
        super().__init__(message, status_code=400, location=location)
