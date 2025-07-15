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

    @recipe_bp.route('/recipes', methods=['GET'])
    def get_recipes():
        name = request.args.get('name')
        query = Recipe.query
        if name:
            query = query.filter(Recipe.name.ilike(f"%{name}%"))
        recipes = query.all()
        result = []
        for recipe in recipes:
            result.append({
                'id': recipe.id,
                'name': recipe.name,
                'description': recipe.description,
                'instructions': recipe.instructions,
                'prep_time': recipe.prep_time,
                'cook_time': recipe.cook_time,
                'servings': recipe.servings,
                'image_url': recipe.image_url,
                'ingredients': [{'id': ing.id, 'name': ing.name} for ing in recipe.ingredients],
                'categories': [{'id': cat.id, 'name': cat.name} for cat in recipe.categories]
            })
        return jsonify(result), 200

    @recipe_bp.route('/recipes/<int:id>', methods=['PUT'])
    def update_recipe(id):
        data = request.get_json()
        recipe = Recipe.query.get(id)
        if not recipe:
            return jsonify({'error': 'Recipe not found'}), 404

        recipe.name = data.get('name', recipe.name)
        recipe.description = data.get('description', recipe.description)
        recipe.instructions = data.get('instructions', recipe.instructions)
        recipe.prep_time = data.get('prep_time', recipe.prep_time)
        recipe.cook_time = data.get('cook_time', recipe.cook_time)
        recipe.servings = data.get('servings', recipe.servings)
        recipe.image_url = data.get('image_url', recipe.image_url)

        ingredient_ids = data.get('ingredient_ids')
        if ingredient_ids is not None:
            recipe.ingredients = Ingredient.query.filter(Ingredient.id.in_(ingredient_ids)).all()

        category_ids = data.get('category_ids')
        if category_ids is not None:
            recipe.categories = Category.query.filter(Category.id.in_(category_ids)).all()

        db.session.commit()
        return jsonify({'message': 'Recipe updated', 'id': recipe.id}), 200

    @recipe_bp.route('/recipes/<int:id>', methods=['DELETE'])
    def delete_recipe(id):
        recipe = Recipe.query.get(id)
        if not recipe:
            return jsonify({'error': 'Recipe not found'}), 404

        db.session.delete(recipe)
        db.session.commit()
        return jsonify({'message': 'Recipe deleted'}), 200