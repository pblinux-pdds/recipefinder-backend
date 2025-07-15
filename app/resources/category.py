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

        return {'message': 'Category created', 'id': category.id}, 201

    def get(self):
        name = request.args.get('name')
        if name:
            category = Category.query.filter_by(name=name).first()
            if category:
                return {'category': {'id': category.id, 'name': category.name}}, 200
            else:
                return {'error': 'Category not found'}, 404
        else:
            categories = Category.query.all()
            result = []
            for category in categories:
                result.append({
                    'id': category.id,
                    'name': category.name
                })
            return {'categories': result}, 200