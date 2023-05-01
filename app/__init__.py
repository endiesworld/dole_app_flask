from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Import the configurations
from global_config import GlobalConfig

database = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'

def create_app(config_class=GlobalConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    database.init_app(app)
    migrate.init_app(app, database)
    login.init_app(app)
    
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.analytics import bp as analytics_bp
    app.register_blueprint(analytics_bp)
    
    return app

from app import models