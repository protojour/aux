from aux.protocol.http.auth.basic import BasicAuthenticator


class Credentials(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password


def basic(username, password):
    return BasicAuthenticator( Credentials(username, password) )





