from flask import render_template
from app import app
from .requests import get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting General sources
    general_sources = get_sources('general')
    print(general_sources)
    title = 'Home-NEWS sources'
    return render_template('index.html', title=title, general_sources=general_sources)

# @app.route('/source/<source_id>')
# def source(source_id):
#     '''
#     view source page function that returns the source and its data
#     '''
#     return render_template('source.html', id = source_id)     