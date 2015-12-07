# Import flask and template operators
from flask import Flask

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.login import LoginManager
from flask.ext.cors import CORS
# Define the WSGI application object
app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = True
login_manager = LoginManager()

login_manager.init_app(app)

# Configurations
app.config.from_object('config')

from flask import redirect


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')


# Importing of variable necessary for creating blueprint
from views.recipes_view import recipe_blueprint
from views.login_view import login_blueprint
from views.user_view import user_blueprint

# Creating blueprint for route
app.register_blueprint(recipe_blueprint)

app.register_blueprint(login_blueprint)

app.register_blueprint(user_blueprint)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404

# Build the database:
# This will create the database file using SQLAlchemy
#db.create_all()
