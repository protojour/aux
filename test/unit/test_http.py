from unittest2 import TestCase
from aux.protocol.http.http import HTTPRequest, HTTPResponse


class HTTP_Test(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_valid_http_GET_request(self):
        request = HTTPRequest('http://localhost:7070/test', 
                              {'method':'GET',
                               'headers': {'Host': 'a.a.a',
                                           'User-Agent': 'Aux/0.1 (X11; Ubuntu; Linux x86_64; rv:24.0)',
                                           'Accept':'text/html',
                                           'Connection': 'Keep-Alive'}})
        self.assertEquals(request.method, 'GET')
        self.assertEquals(len(request.body), 0)

    def test_valid_http_POST_request(self):
        body_content = 'Hello Body'
        request = HTTPRequest('http://localhost:7070/test', 
                              {'method':'GET',
                               'headers': {'Host': 'a.a.a',
                                           'User-Agent': 'Aux/0.1 (X11; Ubuntu; Linux x86_64; rv:24.0)',
                                           'Accept':'text/html'},
                               'body': body_content})
        self.assertEquals(request.body, body_content)

    def test_default_mechanisms(self):
        request = HTTPRequest('http://localhost:7070')
        self.assertEquals(request.url.geturl(), 'http://localhost:7070/')
        self.assertEquals(request.method, 'GET')
        self.assertEquals(request.body, '')
        self.assertEquals(len(request.body), 0)

        
    def test_valid_http_200_response(self):
        response = HTTPResponse(200,
                                {'headers': {'Server': 'auxsrv/0.0.1',
                                             'Date': 'fakedate',
                                             'Connection': 'keep-alive'},
                                 'body': "200 OK"})
        self.assertEquals(response.status, 200)
        self.assertEquals(response.body, "200 OK")
                               
