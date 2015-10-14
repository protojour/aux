from aux import version
from datetime import datetime
import ConfigParser, os
import logging
import shutil

class LogController(object):
    summary = dict()
    config = None
    
    def __init__(self, config):
        self.config = config
        self.loggers = dict()
        self.log_directory = config.options.log_directory
        self.log_console_level = config.options.log_level
        self.log_file_level = config.options.log_level
        if config.options.log_console_level is not None:
            self.log_console_level = config.options.log_console_level
        if config.options.log_file_level is not None:
            self.log_file_level = config.options.log_file_level
        self.log_verbose = config.options.verbose
        self.log_result_server = config.options.log_server
        self.log_run_dir = os.path.join(self.log_directory,
                                        datetime.strftime(datetime.now(), "%Y%m%d-%H%M%S%f"))
        if not os.path.exists(self.log_run_dir):
            os.makedirs(self.log_run_dir)
        logging.basicConfig(level=self.log_file_level,
                            format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
                            filename='%s/all.log' % self.log_run_dir,
                            filemode='w')
        for loggername in ['runtime', 'protocol', 'script', 'systems']:
            self.loggers[loggername] = self.__new_logger(loggername, self.log_run_dir)
            
        if self.log_verbose:
            self.pprint_header_on_init()
            
        self.summary['logs'] = self.log_run_dir
        self.summary['success'] = True #TODO: bad assumption
        config.options.systems = self.copy_systems_file_to_logdir(config.options.systems)
        self.summary['systems'] = config.options.systems
        
        self.runtime.debug('Config options :\n%s' % self.config.options)
        self.runtime.debug('Config arguments :\n %s' % self.config.args)

    def __getattr__(self, attr):
        if self.loggers.get(attr, None) is not None:
            return self.loggers.get(attr)
        else:
            emsg = "%s object has no attribute '%s'" % (self.__class__.__name__, attr)
            raise AttributeError(emsg)

    def __new_logger(self, loggername, logdir):
        new_logger = logging.getLogger(loggername)
        fh = logging.FileHandler(filename=os.path.join(logdir,
                                                       '%s.log' % (loggername)))
        fh.setLevel(self.log_file_level)
        ch = logging.StreamHandler()
        ch.setLevel(self.log_console_level)
        formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s',
                                      '%H:%M:%S')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        new_logger.addHandler(fh)
        new_logger.addHandler(ch)
        new_logger.debug('Initiated')
        return new_logger
        
    def post_to_server(self):
        serverendpoint = self.config.options.log_server
        json_data = {'started' : str(self.summary.get('started')),
                     'ended' : str(self.summary.get('stopped')),
                     'test' : self.summary.get('test'),
                     'success' : self.summary.get('success', False),
                     'testsubject' : str(self.summary.get('testsubject')),
                     'externalref': self.summary.get('externalref'),
                     'tester' : 'auxscript',
                     'logfolder' : self.summary.get('logfolder')}
        headers = {'Host': '192.168.0.135:8080', #TODO: derive from logserverpath
                   'User-Agent':'Aux/0.1 (X11;Ubuntu;Linux x86_64;rv:24.0)',
                   'Cache-Control': 'no-cache'}
        headers.update(http.basic( ('tester', 'tester'))) 
        result = http.post(serverendpoint,
                           headers=headers,
                           body=json.dumps(json_data))

    def pprint_header_on_init(self):
        if self.log_verbose:
            print "-"*70
            self.runtime.info("Options : %s" % (self.config.options))
            self.runtime.info("Args : %s" % (self.config.args))
        
    def pprint_summary_on_exit(self):
        if self.config.options.log_server is not None:
            try: 
                self.post_to_server(self.config.options.log_server)
            except:
                pass
        if self.log_verbose:
            print "-"*70
            print "- AUX %s - Summary" % version()
            print "-"*70
            for key in self.summary.keys():
                print "- %s: %s" % (key, self.summary[key])
            print "-"*70
                
    def copy_systems_file_to_logdir(self, systems):
        newurl = None
        if systems is not None:
            if '.json' in systems:
                url = os.path.abspath(systems)
                newurl = os.path.join(self.log_run_dir, systems)
                shutil.copyfile(url, newurl)
            else:
                newurl = os.path.join(self.log_run_dir, "systems.json")
                fp = open(newurl,"w")
                fp.write(systems)
                fp.close()
            return newurl
        return "No systems set."

        

        
