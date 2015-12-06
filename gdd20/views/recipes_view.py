# -*- encode utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for
from gdd20.api.fast_food_api import FastFoodClient
from flask.ext.login import current_user
from gdd20 import app

recipe_blueprint = Blueprint('recipe_blueprint', __name__, template_folder='templates')
fast_food = FastFoodClient()


@recipe_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template('recipes/index.html', title='Home')


@recipe_blueprint.route('/recipes/', methods=['GET', 'POST'])
def recipes_search():

    # get items search
    items = request.form['items']

    user_likes = []

    if current_user.is_authenticated:
        user_likes = fast_food.get_user_likes(current_user.id)

    # verify item enter empty
    if items == "":
        return redirect(url_for('recipe_blueprint.index'))

    return render_template('recipes/result_search.html',
                           title='Recipes Result',
                           result_recipes=fast_food.get_recipe_by_items(items.encode("utf-8"),
                                                                        True),
                           user_likes=user_likes)


@app.route('/likerecipe')
def like_recipe():
    user_id = request.args.get('user_id')
    recipe_id = request.args.get('recipe_id')
    action = request.args.get('action')
    req = fast_food.like_recipe(user_id=user_id, recipe_id=recipe_id, action=action)
    return req
