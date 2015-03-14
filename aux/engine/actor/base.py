
class BaseActor(object):

    def __init__(self, name):
        self.__is_running = False
        self.name = name

    def is_running(self):
        return self.__is_running

    def set_running(self, state):
        self.__is_running = state
        
    def start(self):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()


