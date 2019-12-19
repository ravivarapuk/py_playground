# Using the inbuild email modeule we can send emial using an already existing email client.
# a program to spam people with promotions
# this lib has beeen updated with Py3 and i'll be using the latest updated module with my Py3


# import the required modules
import os
import sys                                # will allow us to pass the email creds to use the server 
import yaml
import smtplib                            # SMTP -> Simple Mail Transfer Protocol
from email.message import EmailMessage
from string import Template
from pathlib import Path


# setting the arguments/variables
html = Template(Path('index.html').read_text())
email_id = sys.argv[1]
password = sys.argv[2]

root_dir = os.path.dirname(os.path.realpath(__file__))


def _msg_content(username, mailid):
    email = EmailMessage()
    email['name'] = username
    email['to'] = mailid
    email['subject'] = 'You are invited!!!'
    email.set_content(html.substitute({'name'= username}), 'html')
    return email


def _send_email(email_id, password, email):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo() 
        smtp.starttls() # this the encryption mechanism that connects to the server securely
        smtp.login(email_id, password)
        smtp.send_message(email)
        print(f'Worked! Message sent to {email_id}')


def _read_yaml():
    with open(root_dir + '/users.yaml', 'r') as f:
        user_list = yaml.load(f)['EmailIds']
        return user_list[0::2], user_list[1::2]
    


if __name__ == "__main__":
       user_name, user_email = _read_yaml()
       if len(user_name) == len(user_email):
           for x in user_name:
               i = user_name.index(x)
               message_content = _msg_content(x, user_email[i])
               _send_email(email_id, password, message_content)
            print(f'Sent a total of {len(user_name)} emails')
        else:
            raise RuntimeError(f'Error with the structure of the YAML file. Please cheeck it!!!')
