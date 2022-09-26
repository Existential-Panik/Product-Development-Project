from flask import Blueprint, render_template, request, redirect, url_for, flash
import os.path
from .forms import UpdateUserForm, VideoForm
from app.auth.forms import RegistrationForm
from werkzeug.utils import secure_filename
from app.models import Game, db, User

admin_bp = Blueprint(
    "admin_bp", __name__, template_folder="templates/admin", static_folder="/static"
)

ROOT_PATH = os.path.dirname(os.path.join(os.path.dirname(__file__)))

UPLOAD_PATH = os.path.join(ROOT_PATH, "static/uploads")
print(UPLOAD_PATH)


@admin_bp.before_request
def check_is_admin():
    if not request.is_admin:
        return redirect(url_for("auth_bp.main"))


@admin_bp.route("/")
def home():
    users = User.query.all()
    return render_template("admin.html", users=users)


@admin_bp.route("/games/all")
def allgames_page():
    games = Game.query.all()
    return render_template("all-games.html", games=games)


@admin_bp.route("/games/edit/<int:id>", methods=["GET", "POST"])
def edit_game(id):
    game = Game.query.filter(Game.id == int(id))
    form = VideoForm(obj=game.first())
    if form.validate_on_submit():
        name = form.name.data
        url = form.url.data
        thumbnail = form.thumbnail.data
        file_name = secure_filename(thumbnail.filename)
        file_path = os.path.join(UPLOAD_PATH, secure_filename(file_name))
        thumbnail.save(file_path)
        thumbnail = file_name
        game.update(dict(name=name, url=url, thumbnail=thumbnail))
        db.session.commit()
        flash("Game updated successfully")
    return render_template("edit-games.html", form=form)


@admin_bp.route("/games/delete/<int:id>", methods=["GET", "POST"])
def delete_game(id):
    Game.query.filter(Game.id == int(id)).delete()
    db.session.commit()
    return redirect(url_for("admin_bp.allgames_page"))


@admin_bp.route("/games/add", methods=["GET", "POST"])
def addgames_page():
    form = VideoForm()
    if request.method == "POST":
        if form.validate_on_submit():
            name = form.name.data
            url = form.url.data
            thumbnail = form.thumbnail.data
            file_name = secure_filename(thumbnail.filename)
            file_path = os.path.join(UPLOAD_PATH, secure_filename(file_name))
            thumbnail.save(file_path)
            new_game = Game(name=name, url=url, thumbnail=file_name)
            db.session.add(new_game)
            db.session.commit()
            return redirect(url_for("admin_bp.allgames_page"))
    return render_template("add-games.html", form=form)


@admin_bp.route("/users/all")
def allusers_page():
    users = User.query.all()
    return render_template("all-users.html", users=users)


@admin_bp.route("/users/add")
def addusers_page():
    return render_template(
        "add-users.html",
    )


@admin_bp.route("/users/edit/<int:id>", methods=["GET", "POST"])
def editusers_page(id):
    user = User.query.filter(User.id == int(id))
    form = UpdateUserForm(obj=user.first())

    if request.method == "POST":
        print(form.validate_on_submit())
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            password = form.password.data
            user.update(dict(name=name, email=email, password=password))
            db.session.commit()
            flash("User updated Successfully ")
    return render_template("edit-users.html", form=form)


@admin_bp.route("/users/delete/<int:id>")
def delete_user(id):
    User.query.filter(User.id == int(id)).delete()
    db.session.commit()
    return redirect(url_for("admin_bp.allusers_page"))
