from app import app
import urllib.request,json
from .models import article, source

Source = source.Source
Article = article.Article

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the source base url
base_url = app.config["SOURCE_API_BASE_URL"]

#Getting Top news base url
top_base_url = app.config["TOP_API_BASE_URL"]

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results    

def process_results(source_list):
    '''
    Function that processes the source results and transforms it into a list of objects
    '''   

    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if name:
            source_object = Source(id,name,description,url,category,language,country)
            source_results.append(source_object)

    return source_results  

def get_top_articles():
    '''
    Function that gets the json response to our url request
    '''
    get_top_articles_url = top_base_url.format(api_key)

    with urllib.request.urlopen(get_top_articles_url) as url:
        get_top_articles_data = url.read()
        get_top_articles_response = json.loads(get_top_articles_data)

        top_articles_results = None

        if get_top_articles_response['articles']:
            top_articles_results_list = get_top_articles_response['articles']
            top_articles_results = process_results(top_articles_results_list)

    return top_articles_results    

def process_results(top_article_list):
    '''
    Function that processes the top articles and transforms it into a list of objects
    '''   

    top_articles_results = []

    for top_article_item in top_article_list:
        id = top_article_item.get('source[name]')
        name = top_article_item.get('source[name]')
        description = top_article_item.get('description')
        author = top_article_item.get('"author')
        url = top_article_item.get('url')
        title = top_article_item.get('title')
        urlToImage = top_article_item.get('urlToImage')
        publishedAt = top_article_item.get('publishedAt')
        content = top_article_item.get('content')

        if content:
            top_article_object = Article(id,name,description,author,url,title,urlToImage,publishedAt,content)
            top_articles_results.append(top_article_object)

    return top_articles_results           

