from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from endpodints.mail import MailSender, MailReciever, MailReader
from endpodints.news import News, NewsSources

app = Flask(__name__)
api = Api(app)
CORS(app, origins="http://127.0.0.1:8080", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True)

api.add_resource(MailSender, '/mail/send')
api.add_resource(MailReciever, '/mail/fetch')
api.add_resource(MailReader, '/mail')
api.add_resource(News, '/news')
api.add_resource(NewsSources, '/news/sources')
if __name__ == '__main__':
    app.run(port=5000, debug=True)
