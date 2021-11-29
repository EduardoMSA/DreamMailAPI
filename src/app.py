from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from endpodints.mail import MailSender, MailReciever, MailReader
from endpodints.news import News, NewsSources

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(MailSender, '/mail/send')
api.add_resource(MailReciever, '/mail/fetch')
api.add_resource(MailReader, '/mail')
api.add_resource(News, '/news')
api.add_resource(NewsSources, '/news/sources')
if __name__ == '__main__':
    app.run(port=5000, debug=True)
