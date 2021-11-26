import smtplib
import imaplib
from email.parser import Parser
import email
from typing import List

SMTP_SERVER = "smtp.gmail.com"
IMAP_SERVER = 'imap.gmail.com'
SMTP_PORT = 465

class Email:

    def __init__(self, address, password) -> None:
        self.address = address
        self.password = password


    def sendMail(self, msg:str, receiver:str) -> None:

        msg = msg

        s = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        s.login(self.address, self.password)
        s.sendmail(self.address, receiver, msg)
        s.quit()

    def receiveMail(self, since:str = '25-Nov-2021') -> list:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(self.address, self.password)

        mail.select('inbox')
        status, data = mail.search(None, '(SINCE "{}")'.format(since))
        mail_ids = []
        mails = []
        for block in data:
            mail_ids += block.split()

        
        for i in mail_ids:
            status, data = mail.fetch(i, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    message = email.message_from_bytes(response_part[1])
                    mail_id = message['Message-ID']
                    mail_from = message['from']
                    mail_subject = message['subject']
                    mail_date = message['Date']
                    if message.is_multipart():
                        mail_content = ''

                        for part in message.get_payload():
                            if part.get_content_type() == 'text/plain':
                                mail_content += part.get_payload()
                    else:
                        mail_content = message.get_payload()

                    mail_item = {'id':mail_id,'from':mail_from,'date':mail_date,'subject':mail_subject,'content':mail_content}
                    mails.append(mail_item)
            
        return mails

