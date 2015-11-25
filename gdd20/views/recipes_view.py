# -*- encode utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for
from gdd20.api.fast_food_api import FastFoodClient


recipe_blueprint = Blueprint('recipe_blueprint', __name__, template_folder='templates')
fast_food = FastFoodClient()


@recipe_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template('recipes/index.html', title='Home')


@recipe_blueprint.route('/recipes/', methods=['GET', 'POST'])
def recipes_search():

    # get items search
    items = request.form['items']

    # verify item enter empty
    if items == "":
        return redirect(url_for('recipe_blueprint.index'))

    return render_template('recipes/result_search.html',
                           title='Recipes Result',
                           result_recipes=fast_food.get_recipe_by_items(items.encode("utf-8"),
                                                                        True))
