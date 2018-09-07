from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Local Music Home')


@app.route('/list_artists')
def list_artists():
    artists = [
        {'name': 'artist'},
        {'name': 'another artist'}
    ]
    return render_template('list.html', title='Artist List - Local Music', artists=artists)


@app.route('/new_artist')
def new_artist():
    return render_template('new.html', title='New Artist - Local Music')

@app.route('/artist_page')
def artist_page():
    artist = {
        'name': 'artist',
        'bio': 'this artist lived on earth',
        'hometown': 'place',
        'events': ['event 1', 'event2', 'event3']
    }
    return render_template('artist.html', title='Artist Page - Local Music', artist=artist)