import urllib.request,json
from .models import Source,Article

api_key = None
source_url = None
article_url = None

def configRequest(app):
    global api_key,source_url,article_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['NEWS_API_SOURCE_URL']
    article_url = app.config['NEWS_API_ARTICLE']

def getSources(category):

    getSourcesURL = source_url.format(category,api_key)
    

    with urllib.request.urlopen(getSourcesURL) as url:
        getSourcesData = url.read()
        getSourcesResponse = json.loads(getSourcesData)

        sourcesResults = None 

        if getSourcesResponse['sources']:
            sourcesResultsList = getSourcesResponse['sources']
            sourcesResults = processSources(sourcesResultsList)

    return sourcesResults        

def processSources(sourceLists):
    sourcesResults = []
    for sourceList in sourceLists:
        id = sourceList.get('id')
        name = sourceList.get('name')
        description = sourceList.get('description')
        url = sourceList.get('url')
        category = sourceList.get('category')
        language = sourceList.get('language')
        country = sourceList.get('country')

        sourceObject = Source(id,name,description,url,language,category,country)

        sourcesResults.append(sourceObject)

    return sourcesResults
    
def getArticles(id):
    get_article_url = article_url.format(id,api_key)


    with urllib.request.urlopen(get_article_url) as url:
        articleData = url.read()
        articleResponse = json.loads(articleData)
        # import pdb; pdb.set_trace()

        articlesResults = None

        if articleResponse['articles']:
            articlesResultsList = articleResponse['articles']
            articlesResults = processArticles(articlesResultsList)
            

    return articlesResults



def processArticles(articlesList):

    articlesResults = []
    for articleResponse in articlesList:
        author = articleResponse.get('author')
        title = articleResponse.get('title')
        description = articleResponse.get('description')
        urlToImage = articleResponse.get('urlToImage')
        url = articleResponse.get('url')
        publishedAt = articleResponse.get('publishedAt')

        article_object = Article(author,title,description,url,urlToImage,publishedAt)

        articlesResults.append(article_object)


    return articlesResults


def search_movie(news_name):
    search_news_url = 'https://api.themoviedb.org/3/search/news?api_key={}&query={}'.format(
        api_key, news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)
        search_news_results = None
        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_results(search_news_list)
            
    return search_news_results

    