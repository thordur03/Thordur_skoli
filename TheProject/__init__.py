from flask import Flask
from codemodules.config  import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__,template_folder='templates')
    app.config.from_object(Config)

    db.init_app(app)
    
    login_manager.init_app(app)
    login_manager.login_view = "login"
    return app
