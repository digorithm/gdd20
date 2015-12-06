# -*- encode utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for
from gdd20.api.fast_food_api import FastFoodClient
from flask.ext.login import login_user, current_user, logout_user

login_blueprint = Blueprint('login_blueprint', __name__, template_folder='templates')
fast_food = FastFoodClient()


@login_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        login = request.form['email']
        password = request.form['password']
        role = 1
        name = request.form['name']

        fast_food.register_new_user(login, password, role, name)
        return redirect(request.referrer)


@login_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        print "### current_user ### :", current_user

        return render_template('login/login.html', title='Login')

    login = request.form['email']
    password = request.form['password']
    user = fast_food.authenticate_user(login, password)
    login_user(user)

    return redirect('/')


@login_blueprint.route('/logout/', methods=['GET'])
def logout():
    logout_user()
    return redirect('/')
