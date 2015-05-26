from unittest2 import TestCase
from aux.protocol.http import HTTP, HTTPRequest
from ..util.mockhttpserver import MockHTTPSServer

class HTTPSConnectionTest(TestCase):
    
    def setUp(self):
        self.test_server = MockHTTPSServer(port=8443)
        self.test_server.start_thread()

    def tearDown(self):
        self.test_server.stop()

    def xtest_connection_success(self):
        http = HTTP()
        http_request = HTTPRequest({'method':'GET',
                                    'headers': {'Host': 'Aux/0.1 (X11; Ubuntu; Linux x86_64; rv:24.0)',
                                                'User-Agent': 'Aux/0.1 (X11; Ubuntu; Linux x86_64; rv:24.0)',
                                                'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                                'Accept-Language': 'en-US,en;q=0.5',
                                                'Referer': 'http://abc.abc',
                                                'Cache-Control': 'max-stale=0',
                                                'Connection': 'Keep-Alive'
                                                },
                                    'data': 'fakedata'})
        response = http.send('https://127.0.0.l1:8443', http_request)
        self.assertTrue('It works!' in response)



