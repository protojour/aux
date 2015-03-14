# from aux.internals.pluginhook import PluginImporter
import sys
import os
import imp
import device
import service
from aux import systems_pool

#these imports should be kept in a system pool and only be instantiated once.

class SystemNotFoundException(Exception):pass

def scan_files(files, systemtype):
    for f in files:
        fp = open(f,'r')
        if systemtype in fp.read():
            return f
    return None

def find_systemtype(systemtype):
    ## NEED TO LOOKUP IN system.device and system.service and aux_device and aux_service
    ## this implementation is hack and also needs a cache file for aux devices and services so that we only need to scan plugins
    
    foundfile = None
    tmp_filter = ['ext']

    if foundfile is None:
        modulepath = os.path.dirname(device.__file__) #Search through devices
        files = [os.path.join(modulepath,r) for r in os.listdir(os.path.dirname(device.__file__)) if r not in tmp_filter]
        foundfile = scan_files(files, systemtype)

    if foundfile is None:
        modulepath = os.path.dirname(service.__file__) #Search through services
        files = [os.path.join(modulepath,r) for r in os.listdir(os.path.dirname(service.__file__)) if r not in tmp_filter]
        foundfile = scan_files(files, systemtype)    

    if foundfile is None:
        for s in [p for p in sys.path if 'aux_device_' in p]: #Search through plugin devices
            modulepath = imp.find_module(os.path.split(s)[1])[1]
            files = [os.path.join(modulepath,r) for r in os.listdir(modulepath)]
            foundfile = scan_files(files, systemtype)        

    if foundfile is None:
        for s in [p for p in sys.path if 'aux_service_' in p]: #Search through plugin services
            modulepath = imp.find_module(os.path.split(s)[1])[1]
            files = [os.path.join(modulepath,r) for r in os.listdir(modulepath)]
            foundfile = scan_files(files, systemtype)        
        
    if foundfile is not None:
        print foundfile
        module, fx = os.path.split(foundfile)
        mod1 = os.path.split(module)[1]
        fil1 = fx.split('.')[0]
        # print '*'*20
        # print systemtype
        # print foundfile
        # print module
        # print mod1
        # print '*'*20            
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
                  "properties": [{"a":"2"}]}
    '''

    
    if systemjson.get('hostname') is not None:
        #target with specific hostname        
        if systemjson.get('systemtype') is not None:
            hostname = systemjson.get('hostname')
            systemtype = systemjson.get('systemtype')
            return find_systemtype(systemtype)(hostname)
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
                    return find_systemtype(systemtype)(hostname)
                    
    return None
