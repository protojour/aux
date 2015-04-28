import sys
import os
# import device
# import plugin
import pkg_resources

def version():
    return pkg_resources.get_distribution(aux.__package__.title()).version

def base_dir():
    return os.path.abspath(os.path.dirname(aux.__file__))

def working_dir():
    return os.getcwd()

import aux
from aux.logger import LogController
from datetime import datetime
import json
from aux.internals import plugin_creator_routine
from aux.engine import engine_factory

logcontroller = None
configuration = None
systems_pool = []

def run():
    from aux.internals.configuration import config
    global configuration 
    global logcontroller
    global systems_pool
    configuration = config
    if config.options.plugincreator is not None:
        plugin_creator_routine(config.options.plugincreator,
                               config.args)

    ## - read config file
    try:
        config.load_default_properties()
    except Exception, e:
        print 'Falling back to default settings.'
        print e.message

    ## - initiate logger        
    logcontroller = LogController(config)

    ## - Setup
    logcontroller.summary['started'] = datetime.now()

    scripts_as_args = [script for script in config.args if '.py' in script]
    if len(scripts_as_args) != 1:
        logcontroller.runtime.error('Script argument missing')
        sys.exit(1)
    logcontroller.summary['test'] = [ sys.argv[x] for x in range(0, len(sys.argv)) if '.py' in sys.argv[x] ][0]        
    ## - initiate backend
    ## -- start engine
    engine = engine_factory('reactor', config)
    engine.start()
    ## - verify systems
    config.set_systems()
    #configuration.system
    #script
    #TODO: copy script to log_folder
    ## - run
    print(execfile(scripts_as_args[0]))
    ## - do teardown
    engine.stop()
    logcontroller.summary['ended'] = datetime.now()
    
# __all__ = ['device',
#            'plugin',
#            'run']

__all__ = ['run']


def exit_hook():
    if logcontroller is not None:
        logcontroller.pprint_summary_on_exit()
sys.exitfunc = exit_hook
