# -*- encode utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for
from gdd20.api.fast_food_api import FastFoodClient
from flask.ext.login import current_user
from gdd20 import app


user_blueprint = Blueprint('user_blueprint', __name__, template_folder='templates')
fast_food = FastFoodClient()


@user_blueprint.route('/profile/', methods=['GET'])
def profile():
	if not current_user.is_authenticated:
		redirect('/')
	return render_template('user/profile.html', title='Profile')