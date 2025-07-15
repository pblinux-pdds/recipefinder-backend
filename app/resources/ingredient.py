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

    def put(self, id):
        data = request.get_json()
        ingredient = Ingredient.query.get(id)
        if not ingredient:
            return {'error': 'Ingredient not found'}, 404

        name = data.get('name')
        if name:
            ingredient.name = name
            db.session.commit()
            return {'message': 'Ingredient updated', 'id': ingredient.id, 'name': ingredient.name}, 200
        else:
            return {'error': 'No data to update'}, 400

    def delete(self, id):
        ingredient = Ingredient.query.get(id)
        if not ingredient:
            return {'error': 'Ingredient not found'}, 404

        db.session.delete(ingredient)
        db.session.commit()
        return {'message': 'Ingredient deleted'}, 200