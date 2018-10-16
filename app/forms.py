from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, \
    BooleanField, SelectField, SelectMultipleField, DateField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email
from app.models import Artist, User, Venue

class NewArtistForm(FlaskForm):
    name = StringField('Artist Name', validators=[DataRequired()])
    hometown = StringField('Hometown', validators=[DataRequired()])
    bio = TextAreaField('Biography', validators=[DataRequired()])
    submit = SubmitField('Create Artist')

    def validate_name(self, name):
        user = Artist.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('This artist already exists.')

class NewVenueForm(FlaskForm):
    name = StringField('Venue Name', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    submit = SubmitField('Create Venue')

    def validate_name(self, name):
        user = Venue.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('This venue already exists.')

class NewEventForm(FlaskForm):
    name = StringField('Event Name', validators=[DataRequired()])
    date = DateField('Date', format='%m-%d-%Y', validators=[DataRequired()])
    venue = SelectField('Venue', coerce=int, validators=[DataRequired()])
    artists = SelectMultipleField('Artists', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Create Event')

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