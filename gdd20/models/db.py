

class User():

    def __init__(self, id, name, role, email, token):
        self.id = id
        self.name = name
        self.role = role
        self.email = email
        self.token = token
 
    def is_authenticated(self):
        return True

    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.name)
