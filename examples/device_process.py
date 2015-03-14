from aux.scriptengine import ScriptEngine
from aux import api
from getpass import getpass
from aux.device.network import NetworkDevice

engine = ScriptEngine()

def run_command_on_device():
    protocols = {'ssh': {'port': 22, # Optional, defaults to 22
                         #'username': 'root', # Optional, defaults to uid of process
                         'password': getpass()},
                 # 'http': {'port': 80} # Not implemented using this construct...
                 }
    device = NetworkDevice(engine, address='localhost', protocols=protocols)
    out, err, code = device.ssh.run_command('ls')
    print 'stdout:', out, 'stderr:', err, 'exit code:', code


api.run(engine, run_command_on_device)
