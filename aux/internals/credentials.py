

class Credentials(object):
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __call__(self):
        return (self.username, self.password)
        
    def __repr__(self):
        return '(\'%s\', ***)' % (self.username)
        


