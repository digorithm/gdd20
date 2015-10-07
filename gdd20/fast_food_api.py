# -*- encode utf-8 -*-

from api_base import RESTClientJSONBase


class FastFoodClient(RESTClientJSONBase):
    
    def __init__(self, app=None, recipe_id=None):
        
        super(FastFoodClient, self).__init__(None, None)
        self.timeout = 5
        self.init_app()

    def init_app(self):
        self.api_url = 'http://0.0.0.0:8080/api/v1' 
    
    def get_all_recipes(self):
        return self.get('/recipes/').data

    def get_recipe_by_id(self, recipe_id):
        return self.get('/recipes/%d' % recipe_id).data

    def get_recipe_by_items(self, items, restrict):
        return self.get('/recipes/items/items={}&restrict={}'.format(items, restric))
