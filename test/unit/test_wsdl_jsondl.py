from unittest2 import TestCase
# from aux.protocol.rest.jsondl import JSONDL
from aux.protocol.soap.wsdl import WSDLClient
from wsdldatatmp import ssp_wsdl

WSDL_MOCK = '''<wsdl:definitions name="TestService"
   targetNamespace="http://www.examples.com/wsdl/HelloService.wsdl"
   xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
   xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
   xmlns:tns="http://www.examples.com/wsdl/HelloService.wsdl"
   xmlns:xsd="http://www.w3.org/2001/XMLSchema">
   <wsdl:types>
     <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

     </xs:schema>
   </wsdl:types>
   <wsdl:message name="GetTestRequest">
     <wsdl:part element="tns:GetTest" name="GetTestRequest"></wsdl:part>
   </wsdl:message>
   <wsdl:portType name="testsomething">
      <wsdl:operation name="GetTest">

      </wsdl:operation>
   </wsdl:portType>
   <wsdl:service name="TestService">
      
   </wsdl:service>
</wsdl:definitions>
'''


JSONDL_MOCK = '''
{"api": {},
 "types": {}
}
'''


class TestWSDLObject(TestCase):
    def xtest_get_test_request(self):
        wsdl = WSDLClient(wsdl_data=ssp_wsdl)

