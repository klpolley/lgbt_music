from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import Artist

class NewArtistForm(FlaskForm):
    name = StringField('Artist Name', validators=[DataRequired()])
    hometown = StringField('Hometown', validators=[DataRequired()])
    bio = TextAreaField('Biography', validators=[DataRequired()])
    submit = SubmitField('Create Artist')

    def validate_name(self, name):
        user = Artist.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('This artist already exists.')