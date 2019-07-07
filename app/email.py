from flask_mail import Message
from app import mail, App
from flask import render_template
from threading import Thread

def send_async_mail(App, mail):
    with App.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    #mail.send(msg)
    Thread(target=send_async_mail, args=(App, msg)).start()

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Blog] Reset your password', sender=App.config['ADMINS'][0], recipients=[user.email], 
    text_body=render_template('email/reset_password.txt', user=user, token=token), 
    html_body=render_template('email/reset_password.html', user=user, token=token))
