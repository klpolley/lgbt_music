from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email
from app.models import Artist, User

class NewArtistForm(FlaskForm):
    name = StringField('Artist Name', validators=[DataRequired()])
    hometown = StringField('Hometown', validators=[DataRequired()])
    bio = TextAreaField('Biography', validators=[DataRequired()])
    submit = SubmitField('Create Artist')

    def validate_name(self, name):
        user = Artist.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('This artist already exists.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')