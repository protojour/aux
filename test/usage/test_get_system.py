from aux.system import get_system


systemjson = {"hostname": "192.168.0.100",
              "systemtype": "LinuxDevice",
              "username": "username",
              "password": "password"}
vmserver = get_system(systemjson)

print vmserver
print dir(vmserver)
print vmserver.hostname
