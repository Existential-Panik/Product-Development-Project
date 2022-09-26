from flask import Blueprint, render_template, session, request, redirect, url_for
from app.models import User, db
from .forms import RegistrationForm, LoginForm

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
            db.session.commit()
            return redirect(url_for("auth_bp.main"))

    return render_template("signup.html", title="register", form=form)


@auth_bp.route("/forgot_password", methods=["GET", "POST"])
def forgot_pass():
    return render_template("forgot_password.html", title="forgot password")
