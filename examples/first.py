from aux.scriptengine import ScriptEngine
from aux.device.linux import LinuxDevice
from aux import api

engine = ScriptEngine()

def foo():
    device = engine.create_device(LinuxDevice, 'localhost')
    response = device.http.request('GET', '/')
    print response.body

api.run(engine, foo)
