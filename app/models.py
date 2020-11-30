class Source:
    '''
    Class to define news source object
    '''
    def __init__(self, id, name, description, url, category, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country


class Article:
    '''
    A class that defines our articles object
    '''

    def __init__(self, id ,name, title, author, description, url, urlToImage, publishedAt):

        self.id = id
        self.name = name
        self.title = title
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt