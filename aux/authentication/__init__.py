class BaseCredentials(object):
    def __init__(self, ip=None, username=None, password=None, port=None):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
