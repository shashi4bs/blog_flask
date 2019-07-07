from flask import Flask, request 
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel

App = Flask(__name__)
App.config.from_object(Config)

db = SQLAlchemy(App)
migrate = Migrate(App, db)

login = LoginManager(App)
mail = Mail(App)

bootstrap = Bootstrap(App)
moment = Moment(App)
babel = Babel(App)

from app import routes, models, errors

if not App.debug:
    '''
    if App.config['MAIL_SERVER']:
        auth = None
        if App.config['MAIL_USERNAME'] or App.config['MAIL_PASSWORD']:
            auth = (App.config['MAIL_USERNAME'], App.config['MAIL_PASSWORD'])
        secure = None
        if App.config['MAIL_USE_LTS']:
            secure = ()
        mail_handler = SMTPHandler(\
        mailhost = (App.config['MAIL_SERVER'], App.config['MAIL_PORT']),
        fromaddr = 'no-reply@' + App.config['MAIL_SERVER'],\
        toaddrs = App.config['ADMINS'], subject='BLOG Failue',\
        credentials=auth, secure=secure\
        )

    mail_handler.setLevel(logging.ERROR)
    App.logger.addHandler(mail_handler)
    '''
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/blog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s : %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    App.logger.addHandler(file_handler)
    App.logger.setLevel(logging.INFO)
    App.logger.info('Blog Setup')

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
