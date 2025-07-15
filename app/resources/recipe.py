from flask_restful import Resource
from flask import Blueprint, jsonify, request
from app import db
from app.models import Recipe, Ingredient, Category

class RecipeResource(Resource):
    recipe_bp = Blueprint('recipe_bp', __name__)

    @recipe_bp.route('/recipes', methods=['POST'])
    def create_recipe():
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        instructions = data.get('instructions')
        prep_time = data.get('prep_time')
        cook_time = data.get('cook_time')
        servings = data.get('servings')
        image_url = data.get('image_url')
        ingredient_ids = data.get('ingredient_ids', [])
        category_ids = data.get('category_ids', [])

        if not name:
            return jsonify({'error': 'Recipe name is required'}), 400

        ingredients = Ingredient.query.filter(Ingredient.id.in_(ingredient_ids)).all() if ingredient_ids else []
        categories = Category.query.filter(Category.id.in_(category_ids)).all() if category_ids else []

        recipe = Recipe(
            name=name,
            description=description,
            instructions=instructions,
            prep_time=prep_time,
            cook_time=cook_time,
            servings=servings,
            image_url=image_url,
            ingredients=ingredients,
            categories=categories
        )
        db.session.add(recipe)
        db.session.commit()

        return jsonify({'message': 'Recipe created', 'id': recipe.id}), 201