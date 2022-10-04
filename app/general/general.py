from flask import (
    Blueprint,
    render_template,
    request,
    abort,
    session,
    url_for,
    redirect,
    request,
)
from app.models import Game


general_bp = Blueprint(
    "general_bp",
    __name__,
    template_folder="templates/general",
    static_url_path="/static",
)


@general_bp.before_request
def check_is_user_authenticated():
    if not request.is_authenticated:
        return redirect(url_for("auth_bp.main"))


@general_bp.route("/logout")
def logout():
    session.clear()
    return "You are logged out"


@general_bp.route("/")
def home():
    games = Game.query.all()
    return render_template("home.html", games=games)


@general_bp.route("/404")
def error():
    abort(404)
