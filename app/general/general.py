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


general_bp = Blueprint(
    "general_bp",
    __name__,
    template_folder="templates/general",
    static_url_path="/static",
)


@general_bp.before_request
def check_is_user_authenticated():
    print(f"request {request}")
    if not request.is_authenticated:
        redirect(url_for("auth_bp.main"))
    else:
        redirect(url_for("general_bp.home"))


@general_bp.route("/logout")
def logout():
    session.clear()
    return "You are logged out"


@general_bp.route("/")
def home():
    return render_template("home.html", title="Home")


@general_bp.route("/404")
def error():
    abort(404)
