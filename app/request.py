from functools import cached_property
from flask import Request as FlaskRequest, session

from app.models import User


class AnonymousUser:
    @property
    def is_authenticated(self):
        return False

    def __repr__(self) -> str:
        return "<AnonymousUser>"

    @property
    def display_name(self):
        return ""


class Request(FlaskRequest):
    charset = "utf-8"
    encoding_errors = "strict"

    @cached_property
    def user(self):
        user_email = session.get("email", None)
        if user_email:
            return User.query.filter(User.email == user_email).first()
        return AnonymousUser()

    @cached_property
    def is_authenticated(self):
        user_email = session.get("email", None)
        user = User.query.filter(User.email == user_email).first()
        return True if user is not None else False

    @cached_property
    def is_admin(self):
        user_email = session.get("email", None)
        if user_email:
            user = User.query.filter(User.email == user_email).first()
            return user.is_admin if user is not None else False

        return False
