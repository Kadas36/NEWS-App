class Article:
    '''
    Source class defining article object
    '''

    def __init__(self,id,name,description,author,url,title,urlToImage,publishedAt,content):
        self.id = id
        self.name = name
        self.description = description
        self.author = author
        self.url = url
        self.title = title
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content