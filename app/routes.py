from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import NewArtistForm, LoginForm, RegistrationForm, NewVenueForm
from app.models import Artist, Event, ArtistToEvent, Venue, User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
            return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/artists')
def list_artists():
    artists = Artist.query.all()
    return render_template('list.html', title='Artist List', artists=artists)


@app.route('/new_artist', methods=['GET', 'POST'])
@login_required
def new_artist():
    form = NewArtistForm()

    if form.validate_on_submit():
        flash('Artist Created: ' + form.name.data)
        artist = Artist(name=form.name.data.strip(), hometown=form.hometown.data.strip(), bio=form.bio.data.strip())
        db.session.add(artist)
        db.session.commit()

        return redirect(url_for('list_artists'))

    return render_template('new_artist.html', title='New Artist', form=form)

@app.route('/new_venue', methods=['GET', 'POST'])
@login_required
def new_venue():
    form = NewVenueForm()

    if form.validate_on_submit():
        flash('Venue Created: ' + form.name.data)
        venue = Venue(name=form.name.data.strip(), city=form.city.data.strip(), country=form.country.data.strip())
        db.session.add(venue)
        db.session.commit()

        return redirect(url_for('list_artists'))

    return render_template('new_venue.html', title='New Venue', form=form)

@app.route('/artists/<name>')
def artist_page(name):
    artist = Artist.query.filter_by(name=name).first()
    if artist is None:
        flash('Artist "' + name + '" does not exist in the database')
        return redirect(url_for('list_artists'))
    artist_info = {
        'name': artist.name,
        'bio': artist.bio,
        'hometown': artist.hometown,
        'events': artist.events,
    }
    return render_template('artist.html', title=artist.name, artist=artist_info)


@app.route('/reset_db')
def reset_db():
    flash('Resetting Database: deleting old data and repopulating with dummy data')
    # clear all data from all tables
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table {}'.format(table))
        db.session.execute(table.delete())
    db.session.commit()

    # populate tables with dummy data
    artists = [
        Artist(name='Hayley Kiyoko', hometown='Los Angeles, CA', bio='Singer. Songwriter. Actor. Director. Lesbian Jesus.'),
        Artist(name='King Princess', hometown='Brooklyn, CA', bio='This singer-songwriter is known for her personal narrative lyrics'),
        Artist(name='Janelle Monae', hometown='Atlanta, GA', bio='An accomplished musician and actor with a captivating voice'),
        Artist(name='Kehlani', hometown='Oakland, CA', bio='R&B and hip-hop that anyone can get into'),
        Artist(name='The Indigo Girls', hometown='Athens, GA', bio='The iconic, award-winning lesbian folk rock duo'),
        Artist(name='Amythyst Kiah', hometown='Johnson City, TN', bio='A Southern Gothic songster with a hypnotic sound'),
    ]
    db.session.add_all(artists)

    venues = [
        Venue(name='02 Academy Islington', city='London', country='UK'),
        Venue(name='Forum Theatre', city='Melbourne', country='Australia'),
        Venue(name='The Ark', city='Ann Arbor', country='USA'),
        Venue(name='City Park', city='New Orleans, LA', country='USA')
    ]
    db.session.add_all(venues)

    events = [
        Event(name='Expectations Tour 1', date='October 23, 2018', venue=venues[0]),
        Event(name='Expectations Tour 2', date='October 26, 2018', venue=venues[0]),
        Event(name='King Princess Tour', date='November 2, 2018', venue=venues[1]),
        Event(name='King Princess For Real', date='December 17, 2018', venue=venues[2]),
        Event(name='Amy Ray & Her Band', date='November 14, 2018', venue=venues[2]),
        Event(name='Voodoo Music + Arts Experience', date='October 26, 2018', venue=venues[3]),
    ]
    db.session.add_all(events)

    associations = [
        ArtistToEvent(artist=artists[0], event=events[0], headliner=True),
        ArtistToEvent(artist=artists[0], event=events[1], headliner=True),
        ArtistToEvent(artist=artists[3], event=events[1], headliner=False),
        ArtistToEvent(artist=artists[1], event=events[2], headliner=True),
        ArtistToEvent(artist=artists[1], event=events[3], headliner=True),
        ArtistToEvent(artist=artists[4], event=events[4], headliner=True),
        ArtistToEvent(artist=artists[5], event=events[4], headliner=False),
        ArtistToEvent(artist=artists[2], event=events[5], headliner=False),
    ]
    db.session.add_all(associations)

    db.session.commit()

    return redirect(url_for('index'))



