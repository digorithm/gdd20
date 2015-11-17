# -*- encode utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for
from gdd20.api.fast_food_api import FastFoodClient


login_blueprint = Blueprint('login_blueprint', __name__, template_folder='templates')
fast_food = FastFoodClient()


@login_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('login/register.html', title='Login')


@login_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login/login.html', title='Login')
