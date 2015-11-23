# -*- encode utf-8 -*-
from api_base import RESTClientJSONBase
import requests
import json
from gdd20.models.db import User
from gdd20 import login_manager

api_url = 'http://gdd20fastfood.herokuapp.com/api/v1'


class FastFoodClient(RESTClientJSONBase):

    def __init__(self, app=None, recipe_id=None):
        super(FastFoodClient, self).__init__(None, None)
        self.timeout = 10000
        self.init_app()

    def init_app(self):
        self.api_url = 'http://gdd20fastfood.herokuapp.com/api/v1'

    def get_all_recipes(self):
        return self.get('/recipes/').data

    def get_recipe_by_id(self, recipe_id):
        return self.get('/recipes/%d' % recipe_id).data

    def get_recipe_by_items(self, items, restrict):
        return self.get('/recipes/items/?items={}&restrict={}'.format(items, restrict)).data

    # TODO: handle error gracefully
    def register_new_user(self, login, password, role, name):
        data = {'login': login,
                'password': password,
                'role': role,
                'name': name}
        req = requests.post(self.api_url+'/users/', data=data)
        return json.loads(req.text)

    def authenticate_user(self, login, password):
        req = requests.get(self.api_url+'/token', auth=(login, password))
        u = json.loads(req.text)
        user = User(token=u['token'], id=u['user']['id'],
                    name=u['user']['name'], email=u['user']['id'],
                    role=u['user']['role'])
        return user

    @login_manager.user_loader
    def load_user(id):
        data = {'user_id': id}
        req = json.loads(requests.get(api_url+'/users/', data=data).text)

        if not req:
            return None
        user = User(id=id, name=req['name'],
                    role=req['role'],
                    email=req['email'],
                    token=req['password'])
        return user
