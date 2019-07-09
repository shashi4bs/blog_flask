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



#App = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page'
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
babel = Babel()


'''
if not App.debug:
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
    '''

def create_app(config_class = Config):
    App_ = Flask(__name__)
    App_.config.from_object(config_class)

    db.init_app(App_)
    migrate.init_app(App_)
    login.init_app(App_)
    bootstrap.init_app(App_)
    moment.init_app(App_)
    babel.init_app(App_)
    
    if not App_.debug and not App_.testing:
        if App_.config['MAIL_SERVER']:
            auth = None
            if App_.config['MAIL_USERNAME'] or App.config['MAIL_PASSWORD']:
                auth = (App.config['MAIL_USERNAME'], App.config['MAIL_PASSWORD'])
            secure = None
            if App_.config['MAIL_USE_LTS']:
                secure = ()
            mail_handler = SMTPHandler(\
                mailhost = (App.config['MAIL_SERVER'], App.config['MAIL_PORT']),
                fromaddr = 'no-reply@' + App.config['MAIL_SERVER'],\
                toaddrs = App.config['ADMINS'], subject='BLOG Failue',\
                credentials=auth, secure=secure\
            )

            mail_handler.setLevel(logging.ERROR)
            App_.logger.addHandler(mail_handler)
        if App_.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.set_Level(logging.INFO)
            App_.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/blog.log', maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter('%(asctime)s : %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            App_.logger.addHandler(file_handler)
        App_.logger.setLevel(logging.INFO)
        App_.logger.info('Blog Setup')
         
    return App_

App = create_app()

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

from app import routes, models, errors

