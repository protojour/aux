from aux.engine.actor import (Reactor, Proactor, Coactor, NoActorFoundError)
import sys
import traceback

import logging

runtime_log = logging.getLogger('runtime')

class Engine(object):

    def __init__(self, Actor=Reactor, configuration=None):
        self.actor = Actor("Engine")
        
    def setup(self, kwargs):
        self.actor.setup()

    def add_callback(self, callback):
        self.actor.add_callback(callback)

    def remove_callback(self, callback):
        self.actor.remove_callback(callback)
        
    def is_running(self):
        return self.actor.is_running()
        
    def start(self):
        try:
            # self.actor.start()
            # runtime_log.info("Engine started")
            runtime_log.debug("Engine start not implemented")            
        except:
            print traceback.print_exc(file=sys.stdout)

    def stop(self):
        
        try:
            # self.actor.stop()
            # runtime_log.info("Engine stopped")
            runtime_log.debug("Engine stop not implemented")
        except Exception:
            print traceback.print_exc(file=sys.stdout)
        finally:
            if self.is_running():
                pass

def engine_factory(engine_type, config):
    if engine_type.upper()=='REACTOR':
        return Engine(Reactor, configuration=config)
    elif engine_type.upper()=='PROCATOR':
        return Engine(Proactor, configuration=config)
    elif engine_type.upper()=='COACTOR':
        return Engine(Coactor, configuration=config)
    else:
        raise NoActorFoundError(engine_type)
