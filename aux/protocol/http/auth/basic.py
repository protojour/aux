from base64 import b64encode

class BasicAuthenticator(object):

    def __init__(self, credentials):
        self.credentials = credentials

    def __call__(self):
        return {"Basic":"%s" % b64encode(b'%s%s' % (self.credentials.username,
                                                     self.credentials.password))}



    
