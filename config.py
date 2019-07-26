import os
basedir = os.path.abspath(os.path.dirname(__file__))
#load_dotenv(os.path.join(basedir, '.flaskenv'))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    '''postgres://kdehfyahmyrcnx:ccafeab0987183d8f05b1257c8b2e4234b7ee50229eecbe1f6baf75b81f6c2b4@ec2-50-16-197-244.compute-1.amazonaws.com:5432/debadho9t7nuf4'''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #Mail Configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_LTS = os.environ.get('MAIL_USE_LTS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['shashi4bs@gmail.com', 'saar16cs@cmrit.ac.in']
    POSTS_PER_PAGE = 3
    LANGUAGES = ["en", "es"]
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
