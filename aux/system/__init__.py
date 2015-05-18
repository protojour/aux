# from aux.internals.pluginhook import PluginImporter
import sys
import os
import logging
import imp
import device
import service

from aux import systems_pool

log = logging.getLogger('systems')
#these imports should be kept in a system pool and only be instantiated once.

class SystemNotFoundException(Exception):pass

def scan_files(files, systemtype):
    for f in files:
        fp = open(f,'r')
        systemclass = 'class %s' % (systemtype)
        if systemclass in fp.read():
            return f
    return None

def system_filter(systems_list, blacklist):
    def filterout(item):
        for f in blacklist:
            if f in item:
                return False
        return True
    return filter(filterout, systems_list)

def find_systemtype(systemtype):
    ## NEED TO LOOKUP IN system.device and system.service and aux_device and aux_service
    ## this implementation is hack and also needs a cache file for aux devices and services so that we only need to scan plugins
    foundfile = None
    s_filter = ['ext', '.pyc']

    for module in [device, service]:
        if foundfile is None:
            modulepath = os.path.dirname(module.__file__)
            files = system_filter([os.path.join(modulepath,r) for r in os.listdir(modulepath)], s_filter)
            foundfile = scan_files(files, systemtype)

    for plugin_module in ['aux_device_', 'aux_service_']:
        if foundfile is None:
            for s in [p for p in sys.path if plugin_module in p]: 
                modulepath = imp.find_module(os.path.split(s)[1])[1]
                files = system_filter([os.path.join(modulepath,r) for r in os.listdir(modulepath)], s_filter)
                foundfile = scan_files(files, systemtype)        
        
    if foundfile is not None:
        module, fx = os.path.split(foundfile)
        mod1 = os.path.split(module)[1]
        fil1 = fx.split('.')[0]
        if 'aux_' in module:
            modlist = mod1.split('_')
            modlist.insert(1,'system')
            modlist.insert(3, 'ext')
            
        prt = imp.load_module(systemtype, open(foundfile), module, ('','',5))
        return eval("prt.%s" % systemtype)
    raise SystemNotFoundException


def get_system(systemjson):
    '''
    systemjson = {"hostname":"some.name.com.or.ip.10.0.0.1",
                  "systemtype": "MyDevice",
                  "username": "username",
                  "password": "password",
                   "properties": [
                     {"rest.authentication": [
                       {"rest.username":"rduser"},
                       {"rest.password":"yggdrasil"}
                    ]},
                     {"ssh.authentication": [
                       {"rest.username":"rduser"},
                       {"rest.password":"yggdrasil"}
                    ]}]
                 }
    '''
    
    if systemjson.get('hostname') is not None:
        #target with specific hostname        
        if systemjson.get('systemtype') is not None:
            hostname = systemjson.get('hostname')
            systemtype = systemjson.get('systemtype')
            system_instance = find_systemtype(systemtype)(hostname)
            return system_instance
        else:
            #doprobeoftype
            #TODO: this is a bit complex, the probe should be in systemdefinition
            raise NotImplementedError
    else:
        if systemjson.get('systemtype') is not None:
            for system in systems_pool:
                if systemjson.get('systemtype') == system.get('systemtype'):
                    hostname = system.get('hostname')
                    systemtype = system.get('systemtype')
                    system_instance = find_systemtype(systemtype)(hostname)
                    system_instance.inject_properties(system.get('properties'))
                    return system_instance
    return None
