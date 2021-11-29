from typing import Dict
import requests
from datetime import datetime
from helpers.newsFile import readSources
from urllib.request import urlopen 
import base64

API_KEY = '34e1cbeeb82b432e9807b35cab640300'
API_HOST = 'https://newsapi.org/v2/everything'

class NewsHelper:

    def __init__(self) -> None:
        self.sources = readSources()

    def getNews(self, date_from:str = None, language:str = None) -> Dict:
        
        if not date_from:
            date_from = datetime.today().strftime('%Y-%m-%d')
        if not language:
            language = 'es'

        payload = {
            'domains':self.sources,
            'from':date_from,
            'language':language,
            'apiKey':API_KEY,
            'sortBy':'relevancy',
            'pageSize':25
        }

        r = requests.get(API_HOST, payload)

        if r.status_code != 200:
            raise ConnectionError('There is a problem with the server, please check the news sources')

        response = r.json()

        for i in range(len(response['articles'])):
            image = base64.b64encode(urlopen(response['articles'][i]['urlToImage']).read()).decode('utf-8')
            content = response['articles'][i]['content'][:response['articles'][i]['content'].find('[')]
            response['articles'][i]['content'] = content
            response['articles'][i]['image'] = image

        return response

