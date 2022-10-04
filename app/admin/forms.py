from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from app.auth.forms import RegistrationForm


class VideoForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    url = StringField("Url", validators=[DataRequired()])
    thumbnail = FileField("Thumbnail", validators=[FileRequired()])


class UpdateUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])


class AddUserForm(RegistrationForm):
    is_admin = SelectField("Role", choices=[("user", "End User"), ("admin", "Admin")])
    name = StringField(
        "Name",
        validators=[DataRequired(), Length(min=5, max=20)],
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=8)],
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Password must match"),
            Length(min=8),
        ],
    )
    submit = SubmitField("Create User")
