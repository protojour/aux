from unittest2 import TestCase
from aux.protocols.http import HTTPResponse
from .mockhttpserver import WebService, WebServer


class MockHTTPServerTest(TestCase):

    """
    WebService
     - WebService with no app returns 500
     - WebService with success app returns 200
     - 
    """
    
    def test_no_app_defined(self):
        ws = WebService()
        response = ws.call_app()
        self.assertTrue(response.status == 500)

    def test_app_success_defined(self):
        ws = WebService()
        def test_app_ok(environ, start_response):
            return HTTPResponse(200, {'body': 'OK'})
        ws.app = test_app_ok
        response = ws.call_app()
        self.assertTrue(response.status == 200)

    def test_WebService_channel_listener(self):
        pass #Channel

    """
    WebServer
     - Holds a list of services
     - enables service channel listener
     - spawns request handler thread    
    """
    def test_WebServer_list_of_services(self):
        ws1 = WebService()
        ws2 = WebService()
        def test_app_ok(environ, start_response):
            return HTTPResponse(200, {'body': 'OK'})        
        ws1.app = test_app_ok
        ws2.app = test_app_ok
        server = WebServer()
        server.load_service(ws1)
        server.load_service(ws2)
        for service in server.services:
            self.assertTrue(service.call_app().status == 200)

    def test_WebServer_start_server(self):
        ws = WebService()
        def test_app_ok(enviorn, start_response):
            return HTTPResponse(200, {'body': 'OK'})
        ws.app = test_app_ok
        server = WebServer()
        server.load_services([ws, ])
        server.start()
            
