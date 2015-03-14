
class Promise(object):
    def __init__(self):
        self.callbacks = list()

    def addCallbacks(self, callback):
        self.callbacks.append(callback)

        
class Actor(object):
    pass

class Reactor(Actor):
    pass

class Proactor(Actor):
    pass

class Coactor(Actor):
    """
    A Coactor has a realtime queue and an async queue.
    Reactor and Proactor combined.
    """
    pass
