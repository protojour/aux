#-*-auxscript-*-

from aux.device.linux import LinuxDevice


localsystem = LinuxDevice("192.168.0.125")

print localsystem.identifier


localsystem.ssh.set_credentials(('rduser', 'yggdrasil'))

print localsystem.ssh.cmd('ls -al')

print "hello"
