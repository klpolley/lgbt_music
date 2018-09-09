from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='LGBT+Music Home')


@app.route('/list_artists')
def list_artists():
    artists = [
        {'name': 'Hayley Kiyoko'},
        {'name': 'Janelle Monae'},
        {'name': 'King Princess'},
        {'name': 'Tegan and Sara'}
    ]
    return render_template('list.html', title='Artist List - LGBT+Music', artists=artists)


@app.route('/new_artist')
def new_artist():
    return render_template('new.html', title='New Artist - LGBT+Music')

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
    return render_template('artist.html', title='Artist Page - LGBT+Music', artist=artist)