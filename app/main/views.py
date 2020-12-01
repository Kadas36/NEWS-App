from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news, get_articles
from ..models import Source, Article

# Views
@main.route('/')
def index():
    '''
    Function that returns the index page and its data
    '''

    general_list = get_news('general')
    health_list = get_news('health')
    business_list = get_news('business')
    technology_list = get_news('technology')
    sports_list = get_news('sports')
    entertainment_list = get_news('entertainment')

    return render_template('index.html', general=general_list, health=health_list, business=business_list, sports=sports_list, technology=technology_list, entertainment=entertainment_list)               
                                                      

@main.route('/news/<id>')
def news (id):
    '''
    Returns the news article from a highlight
    '''
    news_args = get_articles(id)
    return render_template("articles.html", news=news_args)