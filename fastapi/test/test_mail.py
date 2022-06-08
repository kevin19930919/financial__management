import sys
sys.path.append("../core")
from mail import *
import pytest

class TestMailHandler():
    mail_handler = MailHandler(receiver_email="kevin19930919@gmail.com")

    def test_construct_mail_contents(self):
        content = """
        this is build test
        make sure mail module is working
        """
        self.mail_handler.construct_mail_contents(subject="build test", content=content)

    def test_send_mail(self):
        content = """
        this is build test
        make sure mail module is working
        """
        msg = self.mail_handler.construct_mail_contents(subject="build test", content=content)
        self.mail_handler.send_mail(message=msg)    
