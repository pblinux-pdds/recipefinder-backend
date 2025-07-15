from flask_restful import Resource
from flask import request
from app import db
from app.models import Ingredient

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

    def get(self):
        ingredients = Ingredient.query.all()
        result = []
        for ingredient in ingredients:
            result.append({
                'id': ingredient.id,
                'name': ingredient.name
            })
        return {'ingredients': result}, 200