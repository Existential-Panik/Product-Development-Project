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


@general_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for(".home"))


@general_bp.route("/")
def home():
    games = Game.query.all()
    return render_template("home.html", games=games)


@general_bp.route("/404")
def error():
    abort(404)
