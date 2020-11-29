from flask import render_template
from app import app
from .requests import get_sources, get_top_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    #Getting sources
    all_sources = get_sources()

    #Getting top articles
    top_articles = get_top_articles()

    title = 'Home-NEWS sources'

    return render_template('index.html', title=title, all_sources=all_sources, top_articles = top_articles)
  