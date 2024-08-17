from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
from os import getenv

load_dotenv() # loading env varibles

app = Flask(__name__)

app.config['SECRET_KEY'] = getenv("SECRET_KEY")

if getenv('DEBUG') == 'True': 
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv("SQLALCHEMY_DATABASE_URI_SQLITE")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv("SQLALCHEMY_DATABASE_URI_POSTGRES")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


cache = Cache(
    app, config={"CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 86400000}
)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


from photo_gallery_flask import views
