from flask_restful import Resource
from flask import request
from app import db

class IngredientResource(Resource):
    def post(self):
        data = request.get_json()
        name = data.get('name')

        if not name:
            return {'error': 'Ingredient name is required'}, 400

        ingredient = Ingredient(name=name)
        db.session.add(ingredient)
        db.session.commit()

        return {'message': 'Ingredient created', 'id': ingredient.id}, 201