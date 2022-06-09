"""
    This is an introduction to pydantic library.
"""
from pydantic import BaseModel, validator, ValidationError
from typing import Optional


class User(BaseModel):
    username: str
    password: str
    repeat_password: str
    email: str
    age: Optional[int] = None

    @validator("username")
    def validation_username_length(cls, username):
        if not 3 <= len(username) <= 50:
            raise ValueError("Username must be between 3 and 50 characters long.")

        return username

    @validator("repeat_password")
    def validation_repeat_password_equals_password(cls, repeat_password, values):

        if "password" in values and repeat_password != values["password"]:
            raise ValueError("Passwords do not match.")

        return repeat_password


try:
    user_1 = User(
        username="dbsantiago",
        password="1234",
        repeat_password="1234",
        email="dbsantiago@mail.com"
    )

    print(user_1)

except ValidationError as e:
    print(e.json())
