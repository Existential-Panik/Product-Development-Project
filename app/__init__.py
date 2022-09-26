from flask import Flask, session, redirect, render_template, url_for
from app.general.general import general_bp
from app.auth.auth import auth_bp
from app.admin.admin import admin_bp
from flask_migrate import Migrate

from app.request import Request
from .models import db, User
import os


config = Flask.default_config


class OlympicApp(Flask):
    request_class = Request

    strict_classes = False

    def __init__(self, *args, **kwargs):
        super(OlympicApp, self).__init__(__name__, *args, **kwargs)


DATABASE = os.path.join(os.path.dirname(__file__), "site.db")
migrate = Migrate()


def create_app():
    app = OlympicApp()
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE}"
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()

    app.secret_key = "hhdhdhdhdh7788768"

    @app.before_request
    def check_auth():
        if "email" in session:
            redirect(url_for("general_bp.home"))
        else:
            redirect(url_for("auth_bp.main"))

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html", title="Not Found")

    app.register_blueprint(general_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(admin_bp, url_prefix="/admin")

    @app.cli.command("createsuperuser")
    def createsuperuser():
        """
        Creates new superuser
        """
        name = input("Enter your name ")
        email = input("Enter your unique email ")

        found_user = User.query.filter(User.email == email).first()

        if found_user:
            print("User already exists")
            email = input("Enter your email again ")
        password = input("Enter your password ")
        super_user = User(name=name, email=email, password=password, is_admin=True)
        db.session.add(super_user)
        db.session.commit()

    return app
