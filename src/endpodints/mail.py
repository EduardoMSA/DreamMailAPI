import imaplib
from flask_restful import Resource, reqparse
from helpers.emailHelper import Email
from helpers.emailFile import readData, writeData
from helpers.validator import validateDate, validateEmail, validateInternetConnection


class MailSender(Resource):

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('from', type=str, required=True,
                             help='Email is required', location='json')
    post_parser.add_argument('password', type=str, required=True,
                             help='Password is required', location='json')
    post_parser.add_argument('to', type=str, required=True,
                             help='Email To is required', location='json')
    post_parser.add_argument('message', type=str, required=True,
                             help='MEssage is an required', location='json')

    def post(self):

        if(not validateInternetConnection()):
            return {'message': 'No Internet Connection'}, 502

        data = self.post_parser.parse_args()

        if(not validateEmail(data['from'])):
            return {'message': 'Email From is not valid'}, 400

        if(not validateEmail(data['to'])):
            return {'message': 'Email To is not valid'}, 400

        service = Email(data['from'],data['password'])

        try:
            service.sendMail(data['message'],data['to'])
        except imaplib.IMAP4.error:
            return {'message': 'Wrong Credentials'}, 403

        return {'message': 'Mail Coorectly send to {}'.format(data['to'])}

class MailReciever(Resource):

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('from', type=str, required=True,
                             help='Email is required', location='json')
    post_parser.add_argument('password', type=str, required=True,
                             help='Password is required', location='json')
    post_parser.add_argument('date', type=str, required=True,
                             help='Minimum date to fetch mail (Format 01-Jan-21)', location='json')


    def post(self):

        if(not validateInternetConnection()):
            return {'message': 'No Internet Connection'}, 502

        data = self.post_parser.parse_args()

        if(not validateEmail(data['from'])):
            return {'message': 'Email From is not valid'}, 400

        if(not validateDate(data['date'])):
            return {'message': 'Wrong Date Format, Date must be in the following format: 01-Jan-21'}, 400

        service = Email(data['from'],data['password'])

        try:
            mails = service.receiveMail(data['date'])
        except imaplib.IMAP4.error:
            return {'message': 'Wrong Credentials'}, 403

        writeData(mails, data['from'])

        return {'message': 'Mails correctly fetched and saved','content':mails}

class MailReader(Resource):

    get_parser = reqparse.RequestParser()
    get_parser.add_argument('from', type=str, required=True,
                             help='Email is required', location='args')

    def get(self):

        data = self.get_parser.parse_args()

        if(not validateEmail(data['from'])):
            return {'message': 'Email From is not valid'}, 400

        try:
            mails = readData(data['from'])
        except FileNotFoundError:
            return {'message': 'Email not used previously'}, 404

        return {'message': 'Saved mails correctly fetched','content':mails}


        
        
