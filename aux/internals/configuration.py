import sys        
import os
import json
import logging
from optparse import OptionParser, OptionGroup
from aux import base_dir, systems_pool
from aux.system import get_system

DEFAULT_PROPERTIES_FILE = base_dir()+"/../aux.properties"

def str2loglevel(option, opt_str, value ,parser):
    if value is not None:
        if "DEBUG"==value.upper():
            setattr(parser.values, option.dest, logging.DEBUG)
        elif "INFO"==value.upper():
            setattr(parser.values, option.dest, logging.INFO)
        elif "WARNING"==value.upper():
            setattr(parser.values, option.dest, logging.WARNING)
        elif "ERROR"==value.upper():
            setattr(parser.values, option.dest, logging.ERROR)            
        elif "CRITICAL"==value.upper():
            setattr(parser.values, option.dest, logging.CRITICAL)            
        else:
            setattr(parser.values, option.dest, logging.NOTSET)

def dir2abspath(option, opt_str, value ,parser):
    setattr(parser.values, option.dest, os.path.abspath(value))

            
class Configuration(object):
    def __init__(self):
        self.provision_optargs()

    def provision_optargs(self):
        usage = "usage: aux aux_file.py --option"
        parser = OptionParser(usage=usage)
        parser.add_option("--systems",
                          dest="systems",
                          type="string",
                          help="list of systems")
        parser.add_option("--config",
                          dest="configurationfile",
                          type="string")
        log_group = OptionGroup(parser, "Logging Options")
        log_group.add_option("-v", "--verbose",
                          dest="verbose",
                          action="store_true",
                          default=False,
                          help="verbose to console")
        log_group.add_option("--loglevel",
                          action="callback",
                          callback=str2loglevel,
                          dest="log_level",
                          type="string",
                          default=10,
                          help="[ NOTSET | ERROR | WARNING | INFO | DEBUG ]")
        log_group.add_option("--logconsolelevel",
                          action="callback",
                          callback=str2loglevel,
                          dest="log_console_level",
                          type="string",
                          default=None)
        log_group.add_option("--logfilelevel",
                          action="callback",                          
                          callback=str2loglevel,
                          dest="log_file_level",
                          type="string",
                          default=None)        
        log_group.add_option("--logdir",
                          action="callback",
                          callback=dir2abspath,   
                          dest="log_directory",
                          default=os.path.abspath(os.path.join(base_dir(),
                                                               "..",
                                                               "logs")),
                          type="string")
        log_group.add_option("--logsrv",
                          dest="log_server",
                          type="string")

        tools_group = OptionGroup(parser, "Auxiliary Tools")
        tools_group.add_option("--create_plugin",
                               dest="plugincreator",
                               type="string",
                               help="[ service, device, protocol ]")
        
        parser.add_option("--engine",
                          dest="engine_type",
                          type="string")
        
        parser.add_option_group(log_group)
        parser.add_option_group(tools_group)
        self.options, self.args = parser.parse_args()

    def load_default_properties(self):
        if self.options.configurationfile is None:
            configfilestr = os.path.join(os.path.expanduser("~"), ".aux/aux.properties")
        else:
            configfilestr = self.options.configurationfile
        if not os.path.exists(configfilestr):
            configfilestr = DEFAULT_PROPERTIES_FILE
        fp = open(configfilestr, "r")
        file_configs = json.loads(fp.read())

        if self.options.log_server is None:
            self.options.log_server = file_configs.get('logging').get('resultServer')
        if self.options.log_directory is None:
            self.options.log_directory = file_configs.get('logging').get('logdir')
        if self.options.log_level is None:
            self.options.log_level = file_configs.get('logging').get('loglevel')
        if self.options.log_console_level is None:
            self.options.log_console_level = file_configs.get('logging').get('logconsolelevel')
        if self.options.log_file_level is None:
            self.options.log_file_level = file_configs.get('logging').get('logfilelevel')            
        if self.options.verbose is False:
            self.options.verbose = file_configs.get('logging').get('verbose')
            

    def set_systems(self):
        #populate pool of resources
        system_json = None

        if self.options.systems is not None:
            if '.json' in self.options.systems:
                url = os.path.abspath(self.options.systems)
                fp = open(url, 'r')
                system_json = json.loads(fp.read())
                fp.close()
            else:
                system_json = json.loads(self.options.systems)
        if system_json is not None:        
            for system in system_json:
                systems_pool.append( system )
        
            
config = Configuration() if 'aux' in sys.argv[0] else None

