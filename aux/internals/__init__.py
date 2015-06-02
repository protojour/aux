from aux import working_dir
import os
import sys


def no_plugin_name_message():
    print "No plugin name"
    sys.exit(0)                

def plugin_creator_routine(plugincreator, arguments):
    # print plugincreator, arguments
    plugin_home_directory = working_dir()
    if 'service' in plugincreator:
        if len(arguments) > 0:
            packagename = "_".join(['aux', 'service', arguments[0]])
            os.system('paster create -t basic_package -o %s --no-interactive %s' % (plugin_home_directory,
                                                                                    packagename) )
        else:
            no_plugin_name_message()
    elif 'device' in plugincreator:
        if len(arguments) > 0:
            packagename = "_".join(['aux', 'device', arguments[0]])
            os.system('paster create -t basic_package -o %s --no-interactive %s' % (plugin_home_directory,
                                                                                    packagename))
        else:
            no_plugin_name_message()            
    elif 'protocol' in plugincreator:
        if len(arguments) > 0:
            packagename = "_".join(['aux', 'protocol', arguments[0]])
            os.system('paster create -t basic_package -o %s --no-interactive %s' % (plugin_home_directory,
                                                                                    packagename))
        else:
            no_plugin_name_message()            
    print 'Install plugin by running:\npip install -e %s' % packagename        
    sys.exit(0)


