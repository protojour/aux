from aux.protocols import installers
from aux.device.base import Device

class NetworkDevice(Device):
    """Generic network device
    """
    def __init__(self, scriptengine, address, protocols):
        """
        @param scriptengine: see :Device.__init__:
        @param address: the network address of the device (usually hostname or ip)
        @param protocols: dictionary of protocol names and configurations
                          this Device should be configured with
        """
        Device.__init__(self, address, scriptengine)
        self.address = address

        for protocol, config in protocols.iteritems():
            # Find protocol installers for requested protocols and install on
            # this device with given configuration.
            installer = getattr(installers, protocol)
            installer(self, **config)
