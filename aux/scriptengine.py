print "%s is deprecated" % __file__
from aux.result import ResultCollector
from aux.backend import Backend

class ScriptEngine(object):
    def __init__(self):
        self.logging = None
        self.result_collector = None
        self.backend = None
        self.devices = {}

    def start(self):
        '''
        Initializes the script engine which in turn:

        - Starts the backend
        - Start result collection
        - Initialises logging

        '''
        self.logging = self.start_logging()
        self.result_collector = self.start_result_collector()
        self.backend = self.start_backend()

    def stop(self):
        self.stop_backend()
        self.stop_logging()
        return self.result_collector.get_results()

    def start_logging(self):
        import logging
        logging.basicConfig()
        return None

    def start_result_collector(self):
        result_collector = ResultCollector()
        return result_collector

    def start_backend(self):
        backend = Backend()
        backend.start()
        return backend

    def stop_backend(self):
        self.backend.stop()

    def stop_logging(self):
        pass

    def create_device(self, device_type, identifier, **extra_kwargs):
        if identifier in self.devices:
            return self.devices[identifier]
        device = device_type(identifier, self)
        self.devices[identifier] = device
        return device
