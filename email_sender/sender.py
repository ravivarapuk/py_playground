# Using the inbuild email modeule we can send emial using an already existing email client.
# a program to spam people with promotions
# this lib has beeen updated with Py3 and i'll be using the latest updated module with my Py3


# import the required modules
import os
import sys        # will allow us to pass the email creds to use the server 
import yaml
import smtplib    # SMTP -> Simple Mail Transfer Protocol
from email.message import EmailMessage
from string import Template
from pathlib from Path

html = Template(Path('index.html').read_text())
email_id = sys.argv[1]
password = sys.argv[2]

root_dir = os.path.dirname(os.path.realpath(__file__))


def msg_content(username, mailid):
    email = EmailMessage()
    email['name'] = username
    email['to'] = mailid
    email['subject'] = 'You are invited!!!'
    email.set_content(html.substitute({'name'= username},'html')
    return email


def send_email(email_id, password):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo() 
        smtp.starttls() # this the encryption mechanism that connects to the server securely
        smtp.login(email_id, password)
        smtp.send_message(email)
        print(f'Worked! Message sent to {email_id}')


with open(root_dir + '/users.yaml', 'r') as f:
    user_list = yaml.load(f)['EmailIds']

    if user_list:
