from flask_restful import Resource, reqparse
from helpers.newsHelper import NewsHelper
from helpers.validator import validateInternetConnection, validateLanguage, validateNewsDate, validateNewsSources
from helpers.newsFile import writeData, readData, writeSources, readSources

class News(Resource):
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('lang', type=str, required=False,
                             help='Languague of the articles', location='json')
    post_parser.add_argument('date', type=str, required=False,
                             help='Minimum date to fetch news (Format 2021-01-01)', location='json')

    def post(self):

        if(not validateInternetConnection()):
            return {'message': 'No Internet Connection'}, 502

        data = self.post_parser.parse_args()
        if(data['date'] and not validateNewsDate(data['date'])):
            return {'message': 'Wrong Date Format, Date must be in the following format: 2021-01-01'}, 400
        
        if(data['lang'] and not validateLanguage(data['lang'])):
            return {'message': '{} is not a valid language'.format(data['lang'])}, 400
        
        
        try:
            news = NewsHelper()
            articles = news.getNews(language=data['lang'],date_from=data['date'])
        except ConnectionError:
            return {'message': 'There is a problem with the News Server'}, 202
        except FileNotFoundError:
            return {'message': 'There are no news sources defined'}, 202
        
        writeData(articles)

        return {'message': 'News correctly fetched and saved','content':articles}

    def get(self):
        try:
            articles = readData()
        except:
            return {'message': 'No news saved'}, 404

        return {'message': 'News correctly fetched','content':articles}

class NewsSources(Resource):

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('sources', type=list, required=True,
                             help='List of News Sources', location='json')

    def post(self):
        data = self.post_parser.parse_args()
        if(not validateNewsSources(data['sources'])):
            return {'message': 'At least one source is not valid'}, 400
        if(len(data['sources'])>20):
            return {'message': 'There is a maximum of 20 news sources allowed'}, 400
        writeSources(data['sources'])

        return {'message': 'News` sources correctly saved','content':data['sources']}

    def get(self):
        try:
            sources = readSources()
        except:
            return {'message': 'No news` sources saved'}, 404

        return {'message': 'News` sources correctly fetched','content':sources.split(',')}
        



