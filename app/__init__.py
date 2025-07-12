from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_restful import Api
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    # Import resources
    from app.resources.category import CategoryResource
    from app.resources.ingredient import IngredientResource
    from app.resources.recipe import RecipeResource
    
    # Initialize Flask-RESTful API
    api = Api(app)
    api.add_resource(CategoryResource, '/categories')
    api.add_resource(IngredientResource, '/ingredients')
    api.add_resource(RecipeResource, '/recipes')

    with app.app_context():
        from . import models
        db.create_all()
    return app