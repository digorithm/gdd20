from APIBase import RESTClientJSONBase

class FastFoodClient(RESTClientJSONBase):
    
    
    def __init__(self, app=None):
        
        super(FastFoodClient, self).__init__(None)
        self.timeout = 5
        self.init_app()

    def init_app(self):
        self.api_url = 'http://localhost:8080/api/v1' 
    

    def get_all_recipes(self):
        return self.get('/recipes/')

ffc = FastFoodClient()

print ffc.get_all_recipes()
