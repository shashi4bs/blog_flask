#from app import create_app, db
from app import App, db
from app.models import User, Post
from app import create_app

#App = create_app()
cli.register(App)
@App.shell_context_processor
def make_shell_context():
    return {'db': db, 'User':User, 'Post':Post}
