import os

DATABASE = os.path.join(os.path.dirname(__file__), "site.db")


class Config:
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.mailtrap.io")
    MAIL_PORT = os.environ.get("MAIL_PORT", 2525)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", True)
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL", False)
    MAIL_DEBUG: os.environ.get("MAIL_DEBUG", False)
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME", "97e041d5e367c7")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "cfaf5b99f8bafb")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE}"
