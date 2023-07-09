import smtplib
from email.message import EmailMessage

from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin  # exceptions, models, schemas

from src.auth.utils import get_user_db
from src.config import SMTP_PASSWORD, SMTP_USER
from src.models import Client as User  # , get_user_db

SECRET = "SECRET"
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


def get_email_template_dashboard(user: str):
    email = EmailMessage()
    email['Subject'] = 'Добро пожаловать в fast chat'
    email['From'] = SMTP_USER
    email['To'] = user.email
    email.set_content(
        '<div>'
        f'<h1> Hello,<span style="color:#2764aa"> {user.username} </span></h1>'
        '<div> Вы успешно зарегистрировались! </div>'
        '</div>',
        subtype='html'
    )
    return email


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")
        email = get_email_template_dashboard(user)

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(email)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
