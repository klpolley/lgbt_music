from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    hometown = db.Column(db.String(128))
    bio = db.Column(db.String(256))
    events = db.relationship('ArtistToEvent', back_populates='artist')

    def __repr__(self):
        return '<Artist {}>'.format(self.name)


class ArtistToEvent(db.Model):
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    headliner = db.Column(db.Boolean)
    artist = db.relationship("Artist", back_populates='events')
    event = db.relationship("Event", back_populates='artists')

    def __repr__(self):
        return '<Artist {}, Event {}>'.format(self.artist_id, self.event_id)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    date = db.Column(db.DateTime)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
    artists = db.relationship('ArtistToEvent', back_populates='event')

    def __repr__(self):
        return '<Event {}>'.format(self.name)


class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    city = db.Column(db.String(64))
    country = db.Column(db.String(64))
    events = db.relationship('Event', backref='venue', lazy='dynamic')

    def __repr__(self):
        return '<Venue {}>'.format(self.name)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



@login.user_loader
def load_user(id):
    return User.query.get(int(id))

