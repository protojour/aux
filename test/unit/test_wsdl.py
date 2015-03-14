from unittest2 import TestCase
from aux.protocol.soap.wsdl import WSDLClient


class WSDLTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_basic_wsdl_descriptions_no_attrib(self):
        wsdl_data = "<definitions></definitions>"
        wsdl_object = WSDLClient(wsdl_data = wsdl_data)
        wsdl_object.update_api()
        self.assertEquals(None, wsdl_object.definitions.get('wsdl_data').name)

    def test_basic_wsdl_descriptions_called_definitions(self):
        wsdl_data = '<definitions name="TestService"></definitions>'
        wsdl_object = WSDLClient(wsdl_data = wsdl_data)
        wsdl_object.update_api()
        self.assertEquals('TestService', wsdl_object.defintions.get('wsdl_data').name)

    def test_basic_wsdl_descriptions(self):
        wsdl_data = '<descriptions name="TestService"></descriptions>'
        wsdl_object = WSDLClient(wsdl_data = wsdl_data)
        wsdl_object.update_api()
        self.assertEquals('TestService', wsdl_object.definitions.get('wdsl_data').name)

    def test_basic_wsdl_service(self):
        #TODO: might need tag closure preprocessor
        wsdl_data = """
<descriptions name=\"TestService\" 
   targetNamespace="http://www.examples.com/wsdl/HelloService.wsdl"
   xmlns="http://schemas.xmlsoap.org/wsdl/"
   xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
   xmlns:tns="http://www.examples.com/wsdl/HelloService.wsdl"
   xmlns:xsd="http://www.w3.org/2001/XMLSchema">
   <service name="HelloService">
      <documentation>WSDL File for HelloService</documentation>
      <port binding="tns:Hello_Binding" name="Hello_Port">
         <soap:address
            location="http://www.examples.com/SayHello/"/>
      </port>
   </service>
</descriptions>"""
        wsdl_object = WSDLClient(wsdl_data = wsdl_data)
        service = wsdl_object._w_services[0]
        self.assertEquals("HelloService", service.name)
        self.assertEquals("tns:Hello_Binding", service.ports[0].binding)
        self.assertEquals("Hello_Port", service.ports[0].name)
        self.assertEquals("%saddress" % WSDL.get_ns(service.ports[0].ext_element, "soap"),
                          service.ports[0].ext_element.tag )
        self.assertEquals("http://www.examples.com/SayHello/",
                          service.ports[0].ext_element.attrib.get('location'))

    def test_wsdl_service(self):
        wsdl_data = """
<wsdl:definitions xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:sch2="http://auxiliary.protojour.com/schemas/common" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" targetNamespace="http://auxiliary.protojour.com/schemas/test">
  <wsdl:types>
    <xs:schema xmlns="http://auxiliary.protojour.com/schemas/test" 
               xmlns:ns0="http://auxiliary.protojour.com/schemas/common" 
               xmlns:xs="http://www.w3.org/2001/XMLSchema" 
               attributeFormDefault="unqualified" 
               elementFormDefault="qualified" 
               targetNamespace="http://auxiliary.protojour.com/schemas/test">
      <xs:import namespace="http://auxiliary.protojour.com/schemas/common"/>
      <xs:element name="ListSomethingRequest">
        <xs:annotation>
          <xs:documentation>Request a list of all available code types that can be ordered.</xs:documentation>
        </xs:annotation>
        <xs:complexType/>
      </xs:element>
      <xs:element name="ListSomethingResponse">
        <xs:complexType>
          <xs:sequence>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="codePattern">
              <xs:complexType>
                <xs:attribute name="id" type="xs:string" use="required">
                  <xs:annotation>
                    <xs:documentation>The ID of the code pattern</xs:documentation>
                  </xs:annotation>
                </xs:attribute>
                <xs:attribute name="description" type="xs:string" use="required">
                  <xs:annotation>
                    <xs:documentation>A text description of the code pattern</xs:documentation>
                  </xs:annotation>
                </xs:attribute>
                <xs:attribute name="minLength" type="xs:positiveInteger" use="required">
                  <xs:annotation>
                    <xs:documentation>The minimum code length that can be ordered</xs:documentation>
                  </xs:annotation>
                </xs:attribute>
                <xs:attribute name="defaultLength" type="xs:positiveInteger" use="required">
                  <xs:annotation>
                    <xs:documentation>The default code length of this code pattern</xs:documentation>
                  </xs:annotation>
                </xs:attribute>
                <xs:attribute name="maxLength" type="xs:positiveInteger" use="required">
                  <xs:annotation>
                    <xs:documentation>The maximum code length allowed for this code pattern</xs:documentation>
                  </xs:annotation>
                </xs:attribute>
                <xs:attribute name="caseSensitive" type="xs:boolean" use="required">
                  <xs:annotation>
                    <xs:documentation>Whether this code is case sensitive or not</xs:documentation>
                  </xs:annotation>
                </xs:attribute>
              </xs:complexType>
            </xs:element>
          </xs:sequence>
          <xs:attribute name="defaultCase" type="CodeCase" use="required">
            <xs:annotation>
              <xs:documentation>The default code case if the code is case-insensitive</xs:documentation>
            </xs:annotation>
          </xs:attribute>
        </xs:complexType>
      </xs:element>
      <xs:element name="InitOrderRequest">
        <xs:annotation>
          <xs:documentation>Create a new empty order containing zero codes. Use [expandOrder] to request codes for the order.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
          <xs:sequence>
            <xs:element minOccurs="0" name="type" type="OrderType">
              <xs:annotation>
                <xs:documentation>Deprecated! Do not use</xs:documentation>
              </xs:annotation>
            </xs:element>
            <xs:element default="false" minOccurs="0" name="sectioned" type="xs:boolean">
              <xs:annotation>
                <xs:documentation>Should this order be split into section. Usaually used only with pre-printed media</xs:documentation>
              </xs:annotation>
            </xs:element>
            <xs:element minOccurs="0" name="description" type="xs:string">
              <xs:annotation>
                <xs:documentation>An optional description of the order</xs:documentation>
              </xs:annotation>
            </xs:element>
            <xs:element minOccurs="0" name="productId" type="xs:int">
              <xs:annotation>
                <xs:documentation>An optional product ID. Has to match a previously registered product ID, see [listProducts]</xs:documentation>
              </xs:annotation>
            </xs:element>
            <xs:element minOccurs="0" name="gtin" type="xs:string">
              <xs:annotation>
                <xs:documentation>An optional product GTIN. Has to match a previously registered product's GTIN, see [listProducts]</xs:documentation>
              </xs:annotation>
            </xs:element>
            <xs:element minOccurs="0" name="metadataSchema" type="xs:string">
              <xs:annotation><xs:documentation>An optional meta-data schema ID. Has to match a previously registered schema ID, see [listMetadataSchemas]</xs:documentation>
              </xs:annotation>
            </xs:element>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="InitOrderResponse">
        <xs:complexType>
          <xs:sequence>
            <xs:element name="orderId" type="xs:long">
              <xs:annotation>
                <xs:documentation>The ID of the created order</xs:documentation>
              </xs:annotation>
            </xs:element>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:schema>
  </wsdl:types>
  <wsdl:message name="ListSomethingRequest">
    <wsdl:part element="tns:ListSomethingRequest" name="ListSomethingRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListSomethingResponse">
    <wsdl:part element="tns:ListSomethingResponse" name="ListSomethingResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="InitOrderRequest">
    <wsdl:part element="tns:InitOrderRequest" name="InitOrderRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="InitOrderResponse">
    <wsdl:part element="tns:InitOrderResponse" name="InitOrderResponse">
    </wsdl:part>
  </wsdl:message>

  <wsdl:portType name="auxiliary">
    <wsdl:operation name="ListSomething">
      <wsdl:input message="tns:ListSomethingRequest" name="ListSomethingRequest">
      </wsdl:input>
      <wsdl:output message="tns:ListSomethingResponse" name="ListSomethingResponse">
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="InitOrder">
      <wsdl:input message="tns:InitOrderRequest" name="InitOrderRequest">
      </wsdl:input>
      <wsdl:output message="tns:InitOrderResponse" name="InitOrderResponse">
      </wsdl:output>
    </wsdl:operation>
  </wsdl:portType>

  <wsdl:binding name="AuxiliarySoap11" type="tns:auxiliary">
    <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
    <wsdl:operation name="ListSomething">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListSomethingRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListSomethingResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="InitOrder">
      <soap:operation soapAction=""/>
      <wsdl:input name="InitOrderRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="InitOrderResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
  </wsdl:binding>

  <wsdl:service name="auxiliaryService">
    <wsdl:documentation>Hello</wsdl:documentation>
    <wsdl:port binding="tns:AuxiliarySoap11" name="AuxiliarySoap11">
      <soap:address location="http://127.0.0.1/aux/auxiliary-ws"/>
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
"""
        wsdl_object = WSDLClient(wsdl_data = wsdl_data)
        #message
        print 'debug', wsdl_object.definitions
        self.assertEquals("ListSomethingRequest",
                          wsdl_object.definitions[0].messages[0].name)
        self.assertEquals("ListSomethingResponse",
                          wsdl_object._w_messages[1].name)
        self.assertEquals("InitOrderRequest",
                          wsdl_object._w_messages[2].name)
        self.assertEquals("InitOrderResponse",
                          wsdl_object._w_messages[3].name)
        #service
        self.assertEquals("AuxiliarySoap11",
                          wsdl_object._w_services[0].ports[0].name)
        self.assertEquals("http://127.0.0.1/aux/auxiliary-ws",
                          wsdl_object._w_services[0].ports[0].ext_element.get('location'))
        #binding
        print wsdl_object.ListSomething()
        # self.assertEquals("Service
