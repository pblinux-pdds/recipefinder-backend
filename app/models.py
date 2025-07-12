from . import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
