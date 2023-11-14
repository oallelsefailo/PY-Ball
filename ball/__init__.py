from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pethetic@localhost:5432/ballpy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

    from . import models 
    models.db.init_app(app) 
    migrate = Migrate(app, models.db)

    @app.route('/')
    def home():
        return 'Hello, Ball!'

    return app
