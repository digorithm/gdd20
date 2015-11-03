# -*- encode utf-8 -*-
from flask import Blueprint, render_template, request, abort, json
from gdd20.fast_food_api import FastFoodClient
from gdd20.forms.recipes_form import SearchRecipes


recipes = Blueprint('recipes', __name__, template_folder='templates')
fast_food = FastFoodClient()


@recipes.route('/', methods=['GET', 'POST'])
@recipes.route('/index', methods=['GET', 'POST'])
def index():
	return render_template('recipes/index.html', title='Home', form=SearchRecipes())

@recipes.route('/recipes/items', methods=['GET', 'POST'])
def recipes_items():
	form = SearchRecipes()
	items = form.recipe_item.data
	return render_template('recipes/search.html', 
		title='Recipes Result', 
		result_recipes=fast_food.get_recipe_by_items(items, True))