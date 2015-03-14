from unittest2 import TestCase
from aux.protocols.http import HTTP, HTTPRequest
from ..util.mockhttpserver import MockHTTPServer
import base64


class HTTPAuthenticationTest(TestCase):

    def setUp(self):
        self.test_server = MockHTTPServer(port=8989)
        self.test_server.set_authentication('basic')
        self.test_server.start_thread()

    def tearDown(self):
        self.test_server.stop()

    
    def xtest_basic_authentication(self):
        http = HTTP()
        credentials = ('username', 'password')
        http_request = HTTPRequest({'method':'POST',
                                    'headers': {'Host': 'a.a.a',
                                                'User-Agent': 'Aux/0.1 (X11; Ubuntu; Linux x86_64; rv:24.0)',
                                                'Authorization': 'Basic %s' % base64.b64encode(credentials[0]+credentials[1]),
                                                'Accept':'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                'Accept-Language': 'en-US,en-q=0.5',
                                                'Referer': 'http://abc.abc',
                                                'Cache-Control': 'max-stale=0',
                                                'Connection': 'Keep-Alive'                     
                                                },
                                    'body': 'fakedata'})
        response = http.send('http://127.0.0.1:8989', http_request)
        print 'response', response
        self.assertTrue('200 OK' in response)
        self.assertTrue('<html>' in response)

        
#         http_request = '''\
# GET /basic_authenticated HTTP/1.1
# Host: a.a.a
# User-Agent: Aux/0.1 (X11; Ubuntu; Linux x86_64; rv:24.0)
# Accept: text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Referer: http://abc.abc
# Cache-Control: max-stale=0
# Connection: Keep-Alive
# '''
#         response = conn.send_request(http_request)
#         '''Authorization: Basic QWEtaW46Zm9vYmFy'''
