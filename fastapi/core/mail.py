import smtplib
import mimetypes
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from dataclasses import dataclass
import os

class MailHandler():
    sender = "kevin19930919@gmail.com"
    _user_name = "kevin19930919@gmail.com"
    _password = "qjhuqjoqsvettkqj"

    def __init__(self, receiver_email):
        self.receiver = receiver_email
    
    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, new_receiver):
        self._receiver = new_receiver

    def construct_mail_contents(self, subject, content):
        #initial multipurpose internet mail extension
        mail_contents = MIMEMultipart()
        mail_contents["From"] = self.sender
        mail_contents["To"] = self._receiver
        mail_contents["Subject"] = subject
        mail_contents.attach(MIMEText(content))
        return mail_contents
    
    #define file type
    @classmethod
    def define_file_type(cls, file_path):
        ctype, encoding = mimetypes.guess_type(file_path)
        if not ctype or not encoding:
            ctype = "application/octet-stream"
        return ctype, encoding
    
    @classmethod
    def encode_mime_file(cls, file_path, maintype, subtype):
        with open(file_path, "rb") as fp:
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(fp.read())
        encoders.encode_base64(attachment)
        return attachment

    def send_mail(self, message):
        try:
            with smtplib.SMTP_SSL(host="smtp.gmail.com", port="465") as server: 
                print("login mail server........")
                server.login(self._user_name, self._password)
                print('sending mail')
                server.sendmail(self.sender, self._receiver, message.as_string())
                print('sending mail success')
        except Exception as e:
            print(e)     
        

