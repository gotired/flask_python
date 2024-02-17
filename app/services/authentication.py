"""Authentication Service"""

import bcrypt


class Password:
    """Password Module"""

    def __init__(self, password):
        self.password = password

    async def hash(self):
        """Hash password with salt"""
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(self.password.encode("utf-8"), salt)
        return hashed_password, salt

    async def verify(self):
        """Verify password from database"""
        hashed_password = ""
        return bcrypt.checkpw(self.password.encode("utf-8"), hashed_password)
