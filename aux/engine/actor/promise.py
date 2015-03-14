


class Callback(object):
    def __init__(self, callback_fn):
        pass

class Failure(object):
    pass

class Promise(object):

    def __init__(self):
        self.__callbacks = list()

    def add_callback(self, callbacks):
        self.__callbacks.append(callbacks)



