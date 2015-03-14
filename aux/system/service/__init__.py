# -*- coding: utf-8 -*-

from aux.system.base import BaseSystem

class Service(BaseSystem):
    def __init__(self, hostname):
        super(Service, self).__init__(hostname)
        self.hostname = hostname

