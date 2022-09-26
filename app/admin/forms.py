from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


class VideoForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    url = StringField("Url", validators=[DataRequired()])
    thumbnail = FileField("Thumbnail", validators=[FileRequired()])


class UpdateUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
