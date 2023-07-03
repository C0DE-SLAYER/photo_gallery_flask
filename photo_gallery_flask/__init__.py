from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('../config.py')
cache = Cache(app,config={'CACHE_TYPE': 'SimpleCache','CACHE_DEFAULT_TIMEOUT':86400000})
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



from photo_gallery_flask import views
