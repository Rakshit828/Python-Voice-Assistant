# from config.settings import NEWS_API_KEY
from newsapi import NewsApiClient


newsapi = NewsApiClient(api_key='e82a2208855e46fbb120151bc1bf7da7')



def get_top_headlines():
    top_headlines = newsapi.get_top_headlines(
        q='AI',
        category='technology',
        language='en',
        country='us'
    )
    for i in range(0, get_top_headlines['']):
        print(top_headlines['articles'][i]['title'])


get_top_headlines()


