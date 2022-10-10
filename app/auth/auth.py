from flask_mail import Message
from app.config import Config
from flask import (
    Blueprint,
    render_template,
    session,
    request,
    redirect,
    url_for,
    flash,
)
from uuid import uuid1
from app.models import Token, User, db
from .forms import ChangePasswordForm, ForgotPasswordForm, RegistrationForm, LoginForm
from sqlalchemy.exc import IntegrityError
from app.utils.email import mail

auth_bp = Blueprint("auth_bp", __name__, template_folder="templates/auth")


@auth_bp.route("/login", methods=["GET", "POST"])
def main():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            verify_user = User.query.filter(
                User.email == email, User.password == password
            ).first()
            if verify_user:
                session["email"] = email
                return redirect(url_for("general_bp.home"))
            else:
                flash("Invalid credentials", "error")

    return render_template("login.html", title="Login", form=form)


@auth_bp.route("/register", methods=["GET", "POST"])
def signup():
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            password = form.password.data
            new_user = User(name=name, email=email, password=password)
            db.session.add(new_user)

            try:
                db.session.commit()
            except IntegrityError:
                flash("User already exists", "error")
            return redirect(url_for("auth_bp.main"))

    return render_template("signup.html", title="register", form=form)


@auth_bp.route("/forgot_password", methods=["GET", "POST"])
def forgot_pass():
    form = ForgotPasswordForm()
    if request.method == "POST":
        if form.validate_on_submit():
            email = form.email.data
            user = User.query.filter(User.email == email).first()
            if not user:
                flash(
                    "The user with this email doesn't exist. Please try again!!",
                    "danger",
                )
            else:
                code = str(uuid1())[:6]
                new_token = Token(email=user.email, code=code)
                db.session.add(new_token)
                db.session.commit()
                url = url_for(".reset_pass", code=code, email=user.email)
                msg = Message(
                    f"{user.name}",
                    sender=f"{Config.MAIL_USERNAME}@mailtrap.io",
                    recipients=[user.email],
                )
                msg.html = render_template(
                    "email.html", name=user.name, url=f"localhost:5000{url}"
                )
                mail.send(msg)
                flash(
                    "Reset link sent to your email successfully",
                    "success",
                )

    return render_template("forgot_password.html", form=form)


@auth_bp.route("/reset", methods=["GET", "POST"])
def reset_pass():
    form = ChangePasswordForm()
    email = request.args.get("email")
    code = request.args.get("code")

    token = (
        Token.query.filter(Token.email == email, Token.code == code)
        .order_by(Token.created_at.desc())
        .first()
    )

    if token is None:
        error = "Token doesn't exist"
        return render_template("reset.html", error=error)

    if request.method == "POST":
        if form.validate_on_submit():
            password = form.password.data
            user = User.query.filter(User.email == email).first()
            user.password = password
            db.session.commit()
            return redirect(url_for("auth_bp.main"))

    return render_template("reset.html", form=form)


@auth_bp.route("/verify", methods=["GET", "POST"])
def otp_page():
    return render_template("otp_page.html")
