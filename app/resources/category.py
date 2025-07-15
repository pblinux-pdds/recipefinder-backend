from flask_restful import Resource
from flask import request
from app import db
from app.models import Category

class CategoryResource(Resource):
    def post(self):
        data = request.get_json()
        name = data.get('name')

        if not name:
            return {'error': 'Category name is required'}, 400

        category = Category(name=name)
        db.session.add(category)
        db.session.commit()

        return {'message': 'Category created', 'id': category.id},