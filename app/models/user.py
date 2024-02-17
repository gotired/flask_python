"""Module for validate user model"""

from pydantic import BaseModel, EmailStr, field_validator

from app.services.authentication import Password


class Register(BaseModel):
    """
    User Model Validators
    """

    first_name: str
    last_name: str
    email: EmailStr
    username: str
    password: str

    @field_validator("password")
    @classmethod
    def has_password(cls, value: str):
        """Hash password"""
        hash_password, salt = Password(value.get).hash()
        return {"password": hash_password, "salt": salt}
