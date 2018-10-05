from app import db

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    hometown = db.Column(db.String(128))
    bio = db.Column(db.String(256))
    events = db.relationship('ArtistToEvent', back_populates='artist', lazy='dynamic')

    def __repr__(self):
        return '<Artist {}>'.format(self.name)


class ArtistToEvent(db.Model):
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    headliner = db.Column(db.Boolean)
    artist = db.relationship("Artist", back_populates='events', lazy='dynamic')
    event = db.relationship("Event", back_populates='artists', lazy='dynamic')

    def __repr__(self):
        return '<Artist {}, Event {}>'.format(self.artist_id, self.event_id)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    date = db.Column(db.String(64))
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
    artists = db.relationship('ArtistToEvent', back_populates='event', lazy='dynamic')

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
