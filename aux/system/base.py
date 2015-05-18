import base64
import logging

log = logging.getLogger("systems")

class Authentication(object):
    #TODO: this responsibility should be moved out of base system definition
    class BasicAuth(object):
        basic = None
        def __call__(self, json_data):
            self.basic = json_data.get('base64', None)
            if self.basic is None:
                self.basic = base64.b64encode("%s:%s" % (json_data.get('username'),
                                                         json_data.get('password') ))
                log.debug("Basic authentication credentials changed")
        def __repr__(self):
            return self.basic

        def dict(self):
            return {"Authorization" : "Basic %s" % self.basic}
        
    class SSHAuth(object):
        username = None
        password = None
        cert = None
        
        def __call__(self, json_data):
            self.username = json_data.get('username')
            self.password = json_data.get('password')

        def __repr__(self):
            return "Username: %s, Password: ***" % (self.username)
        
    ssh = SSHAuth()
    basic = BasicAuth()
    digest = None
    ntlm = None
    
class BaseSystem(object):
    def __init__(self, identifier):
        self.identifier = identifier
        self.authentication = Authentication()

    def inject_property(self, _property, value):
        """
        Opportunistically try to set properties.
        Assume that properties defined in configuration exist for given system.
        """
        path = _property.split('.')
        root = self.__getattribute__(path[0])
        prop = root.__getattribute__(path[1])
        prop(value)
        
    def inject_properties(self, properties):
        if properties is not None:
            for p in properties:
                key = p.keys()[0]
                self.inject_property(key, p.get(key))

