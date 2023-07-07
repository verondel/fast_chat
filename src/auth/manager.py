from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin  # exceptions, models, schemas

from src.database import Client as User, get_user_db

SECRET = "SECRET"


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")
        # TODO добавить письмо на почту


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
