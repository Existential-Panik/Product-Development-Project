from flask import session


def is_authenticated():
    return "email" in session
