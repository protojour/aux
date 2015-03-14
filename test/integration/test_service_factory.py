from unittest2 import TestCase
from aux.service.servicefactory import service_factory
from aux.protocols.http import HTTPRequest as Request


class FactoryServiceTest(TestCase):

    def xtest_http_service(self):

        service = service_factory('https')
        request = Request({'method': 'GET',
                           'headers': ['Content-Type: application/json',
                                       'Accept-Type: application/json'],
                           'data': "Test"
                           })
        service.get(request)
