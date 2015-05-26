from unittest2 import TestCase
from aux.api import http


class HTTP_API_Test(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def xtest_http_get(self):
        response = http.get(url="http://test")

    def xtest_http_post(self):
        response = http.post(url="http://test/postresource",
                             headers={})
                             
    def xtest_http_post_with_basic_authentication(self):
        response = http.post(url="http://test/postresource_with_basic_auth")

        
