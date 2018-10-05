from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import NewArtistForm
from app.models import Artist, Event, ArtistToEvent, Venue

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/list_artists')
def list_artists():
    artists = [
        {'name': 'Hayley Kiyoko'},
        {'name': 'Janelle Monae'},
        {'name': 'King Princess'},
        {'name': 'Tegan and Sara'}
    ]
    return render_template('list.html', title='Artist List', artists=artists)


@app.route('/new_artist', methods=['GET', 'POST'])
def new_artist():
    form = NewArtistForm()

    if form.validate_on_submit():
        flash('Artist Created: ' + form.name.data)
        artist = {
            'name': form.name.data,
            'bio': form.bio.data,
            'hometown': form.hometown.data,
            'events': []
        }
        return render_template('artist.html', title='ArtistPage', artist=artist)

    return render_template('new.html', title='New Artist', form=form)

@app.route('/artist_page')
def artist_page():
    artist = {
        'name': 'Hayley Kiyoko',
        'bio': 'Hayley Kiyoko is a 27-year-old American singer, songwriter, actor, dancer, and director.'
               ' Her debut studio album Expectations was released on March 30, 2018.',
        'hometown': 'Los Angeles, CA',
        'events': ['October 23: 02 Academy Islington, London, UK',
                   'October 24: Club Academy, Manchester, UK',
                   'October 26: 02 Academy Islington, London, UK']
    }
    return render_template('artist.html', title='Artist Page', artist=artist)


@app.route('/reset_db')
def reset_db():
    flash("Resetting Database: deleting old data and repopulating with dummy data")
    # clear all data from all tables
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table {}'.format(table))
        db.session.execute(table.delete())
    db.session.commit()

    # populate tables with dummy data
    artists = [
        Artist(name="Hayley Kiyoko", hometown='Los Angeles, CA', bio=''),
        Artist(name="King Princess", hometown='Brooklyn, CA', bio=''),
        Artist(name="Janelle Monae", hometown='Atlanta, GA', bio=''),
        Artist(name="Kehlani", hometown='Oakland, CA', bio=''),
        Artist(name="Mary Lambert", hometown='Seattle, WA', bio='')
    ]
    db.session.add_all(artists)

    venues = [
        Venue(name='02 Academy Islington', city='London', country='England'),
        Venue(name='Forum Theatre', city='Melbourne', country='Australia')
    ]
    db.session.add_all(venues)

    events = [
        Event(name='Expectations Tour 1', date='October 23, 2018', venue=venues[0]),
        Event(name='Expectations Tour 2', date='October 26, 2018', venue=venues[0]),
        Event(name='King Princess Tour', date='November 2, 2018', venue=venues[1]),
    ]
    db.session.add_all(events)

    associations = [
        ArtistToEvent(artist=artists[0], event=events[0], headliner=True),
        ArtistToEvent(artist=artists[0], event=events[1], headliner=True),
        ArtistToEvent(artist=artists[3], event=events[1], headliner=False),
        ArtistToEvent(artist=artists[1], event=events[2], headliner=True),
    ]
    db.session.add_all(associations)

    db.session.commit()

    return redirect(url_for('index'))



