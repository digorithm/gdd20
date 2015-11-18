# -*- encode utf-8 -*-
from api_base import RESTClientJSONBase
import requests
import json


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

    def register_new_user(self, login, password, role, name):
        data = {'login': login,
                'password': password,
                'role': role,
                'name': name}
        req = requests.post(self.api_url+'/users/', data=data)
        return json.loads(req.text)
