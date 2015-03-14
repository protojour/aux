from unittest2 import TestCase
from aux.protocols.soap import create_wsdl
from ..util.mockhttpserver import MockHTTPSServer

class WSDLObjectTest(TestCase):

    def setUp(self):
        self.test_server = MockHTTPSServer(port=8443)
        self.test_server.start_thread()

    def tearDown(self):
        self.test_server.stop()

    def xtest_create_soap_object_from_wsdl(self):
        wsdl_url = "../data/geoipservice.asmx?WSDL"
        wsdl = create_wsdl(wsdl_url)

        # print wsdl.GeoIPContext()
        print wsdl.GetGeoIP()
 
    def xtest_create_soap_object_from_https_wsdl(self):
        wsdl_url = "https://127.0.0.1:8443/geoipservice.asmx?WSDL"
        wsdl = create_wsdl(wsdl_url)

        # print "Wsdl service name:", wsdl.name
        #print wsdl.GetGeoIPContext()
        #print wsdl.GetGeoIP()
