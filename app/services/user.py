"""User Collection Service"""

import uuid
from bson import ObjectId

from app.services.database import MongoDB
from app.utils.error import InsertError


class User:
    """User Collection Service"""

    location = "services/user"
    collection = MongoDB().collection("user_collection")

    @classmethod
    async def check(cls, email: str) -> bool:
        """Validate user in collection"""
        return cls.collection.find_one({"email": email})

    @classmethod
    async def register(cls, user_detail: dict) -> None:
        """register user in collection"""
        check_email_bool = await cls.check(user_detail.get("email"))
        if not check_email_bool:
            user_uuid = uuid.uuid4()
            result = cls.collection.insert_one(
                {**user_detail, "_id": ObjectId(str(user_uuid))}
            )
            if not result.acknowledged:
                raise InsertError(
                    message="Error inserting user",
                    location=f"{cls.location}/register",
                )
        raise ValueError("User is already registered")
