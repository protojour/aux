from unittest2 import TestCase
from aux.protocols import soap
from aux.protocols.http import HTTPRequest
from ..util.mockhttpserver import MockHTTPSServer

class SOAPHTTPSConnectionTest(TestCase):


    def setUp(self):
        self.test_server = MockHTTPSServer(port=8443)
        self.test_server.set_authentication("Basic")
        self.test_server.start_thread()

    def tearDown(self):
        self.test_server.stop()

    def xtest_request_handles_basic_auth_required(self):
        conn = soap.connection('127.0.0.1:8443')
#         wsdl_request = '''
# POST https://aux.protojour.com/ws/test-ws HTTP/1.1
# Content-Type: text/xml;charset=UTF-8
# SOAPAction: ""
# Content-Length: 352
# Host: aux.protojour.com
# Connection: Keep-Alive
# User-Agent: Apache-HttpClient/4.1.1 (java 1.5)

# <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="test" xmlns:com="test">
#    <soapenv:Header/>
#    <soapenv:Body>
#       <ns:ListSomething max="25">
#       </ns:ListSomething>
#    </soapenv:Body>
# </soapenv:Envelope>
# '''
#         response = conn.send_request(wsdl_request)
        
    def xtest_get_products_list(self):
        pass
        
#         wsdl = 'some.wsdl'

#         conn = soap.connection('soap://127.0.0.1:8443')
#         wsdl_request = HTTPRequest({'method': 'POST',
#                                     'headers': {'Accept-Encoding': 'gzip,deflate',
#                                                 'Content-Type': 'text/xml;charset=UTF-8',
#                                                 'SOAPAction': '""',
#                                                 'Authorization': 'Basic abcdefghijklmnopqrstuvwx',
#                                                 'Content-Length': '352',
#                                                 'Host': 'aux.protojour.com',
#                                                 'Connection': 'Keep-Alive',
#                                                 'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)'
#                                                 },
#                                     'data' : '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="test" xmlns:com="test">
#    <soapenv:Header/>
#    <soapenv:Body>
#       <ns:ListSomething max="25">
#       </ns:ListSomething>
#    </soapenv:Body>
# </soapenv:Envelope>'''})
#         response = conn.send_request(wsdl_request)

#         print response
#         self.assertTrue('<SOAP-ENV:Envelop' in response)
    
