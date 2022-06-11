from celery import Celery 
import yaml
from core.mail import *


with open(r'./fastapi/config/config.yaml', 'r') as file:
    config = yaml.full_load(file)

app = Celery(
    "tasks", 
    broker=f'amqp:{config["rabbitmq_user"]}:{config["rabbitmq_password"]}//localhost:5672', 
    backend='rpc://'
) 
 
@app.task 
def send_craw_report(receiver, subject, content):
    try:
        mail_handler = MailHandler(receiver_email=receiver)
        msg = mail_handler.construct_mail_contents(subject=subject, content=content)
        mail_handler.send_mail(message=msg)
        return True
    except Exception as e:
        print(e)
        return False    