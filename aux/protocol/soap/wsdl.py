from aux.protocol.soap import SOAPRequest, SOAPResponse
from lxml import objectify
from lxml import etree
from urlparse import urlparse
from aux.api import http
import os
import logging

log = logging.getLogger("protocol")

class WSDLPort(object):
    def __init__(self, e):
        self.e = e
        self.name = e.get('name')
        self.binding = e.attrib.get('binding')
        self.ext_element = e.getchildren()[0]

class WSDLPortType(object):
    def __init__(self, e):
        self.e = e
        self.name = self.e.get('name')
        self.operations = [WSDLOperation(o) for o in self.e.findall('%soperation' % WSDLClient.get_ns(self.e, 'wsdl'))]

#WIKI: Also reads as PortType in old definition        
class WSDLInterface(WSDLPortType):pass

class XMLComplexType(object):
    def __init__(self, e):
        self.e = e
        # print etree.tostring(e)
        # print 
        self.seq = self.e.findall('%ssequence' % WSDLClient.get_ns(self.e, 'xs'))
        elems = None
        if len(self.seq) > 0:
            elems = [e for e in self.seq[0].findall('%selement' % WSDLClient.get_ns(self.e, 'xs'))]
        if elems is None:
            self.elements = []
        else:
            self.elements = elems
            # for el in elems:
                # print el.get('name')
                # print el.get('type')
                # print etree.tostring(el)
                # print

            
class XMLSimpleType(object):
    def __init__(self, e):
        self.e = e
        
        
class WSDLElement(object):    #WIKI: XML Element SimpleType|ComplexType
    def __init__(self, e):
        self.e = e
        self.name = self.e.get('name')
        self.subelements = [XMLComplexType(se) for se in self.e.findall('%scomplexType' % WSDLClient.get_ns(self.e, 'xs'))]
        self.subelements.extend([XMLSimpleType(se) for se in self.e.findall('%ssimpleType' % WSDLClient.get_ns(self.e, 'xs'))])

class WSDLSchema(object):
    def __init__(self, e):
        self.e = e
        self.elements = [WSDLElement(elem) for elem in e.findall('%selement' % WSDLClient.get_ns(e, 'xs'))]

    
class WSDLTypes(object):
    def __init__(self, e):
        self.e = e
        self.schemas = [WSDLSchema(s) for s in self.e]
        

class WSDLMessagePart(object):
    def __init__(self, e):
        self.e = e
        if self.e is not None:
            self.name = e.get('name')
            self.element = e.attrib.get('element')
        
class WSDLMessage(object):
    def __init__(self, e):
        self.e = e
        if self.e is not None:
            self.name = self.e.get('name')
            self.part = WSDLMessagePart(self.e.find('%spart' % WSDLClient.get_ns(self.e,
                                                                           'wsdl')))

class WSDLOperation(object):
    def __init__(self, e):
        self.e = e
        self.name = self.e.get('name')
        self.input = WSDLMessage( self.e.find('%sinput' % WSDLClient.get_ns(self.e,
                                                                      'wsdl')) )
        self.output = WSDLMessage( self.e.find('%soutput' % WSDLClient.get_ns(self.e,
                                                                        'wsdl')) )

class WSDLBinding(object):
    def __init__(self, e):
        self.e = e
        self.name = e.get('name')
        self.type = e.get('type')
        self.soap_binding = e.find('%sbinding' % WSDLClient.get_ns(e, 'soap'))
        self.operations = [WSDLOperation(o) for o in e.findall('%soperation' % WSDLClient.get_ns(e, 'wsdl'))]
        #self.soap_operation = ?
        
    
class WSDLService(object):
    def __init__(self, e):
        self.name = e.get('name')
        ns = '{%s}' % e.nsmap.get('wsdl') if e.nsmap.get('wsdl') else '{%s}' % e.nsmap.get(None)
        self.documentation = e.find('%sdocumentation' % ns)
        self.ports = [WSDLPort(p) for p in e.findall('%sport' % ns)]
    

class WSDLDefinitions(object):
    def __init__(self, e):
        self.e = e
        # print etree.tostring(self.e)
        self.name = e.get('name')
        self.types = [WSDLTypes(t) for t in self.e.findall('%stypes' % WSDLClient.get_ns(self.e, 'wsdl'))]
        self.messages = [WSDLMessage(m) for m in self.e.findall('%smessage' % WSDLClient.get_ns(self.e, 'wsdl'))]
        self.portType = WSDLPortType(self.e.find('%sportType' % WSDLClient.get_ns(self.e, 'wsdl')))
        self.binding = WSDLBinding(self.e.find('%sbinding' % WSDLClient.get_ns(self.e, 'wsdl')))
        self.service = WSDLService(self.e.find('%sservice' % WSDLClient.get_ns(self.e, 'wsdl')))
        

class WSDLClient(object):

    def __init__(self, wsdl_url=None, wsdl_data=None):
        #WIKI: descriptions is often called definitions.
        self.wsdl_data = wsdl_data
        self.__api_sources = list()
        self.definitions = dict()

    def set_api_source(self, new_api_source_dsn):
        self.__api_sources.append(new_api_source_dsn)

    def get_api_sources(self):
        return self.__api_sources

    def update_api(self):
        if len(self.get_api_sources()):
            for source in self.get_api_sources():
                self.load_wsdl(source.split('/')[-1].replace('.wsdl',''),
                               self.get_proxy(source))
        else:
            self.load_wsdl('wsdl_data', wsdl_data=self.wsdl_data)

    @classmethod
    def get_ns(cls, element, namespace):
        return '{%s}' % element.nsmap.get(namespace) if element.nsmap.get(namespace) else '{%s}' % element.nsmap.get(None)
    
    def load_wsdl(self, definition_name, wsdl_url=None, wsdl_data=None):
        wsdl_string = None
        if wsdl_url is not None:
            wsdl_string = http.get(wsdl_url,
                                   headers=self.headers).body
        elif wsdl_data is not None:
            wsdl_string = wsdl_data
        if wsdl_string is not None:
            resource = etree.XML(wsdl_string)
            self.definitions[definition_name] = WSDLDefinitions(resource)
            
    def __getattr__(self, attr):
        class WSDLo(object):
            def __init__(self, self_instance, definition):
                self.instance = self_instance
                self.definition = definition
                
            def __getattr__(self, attr):
                self.operation = [o for o in self.definition.portType.operations if o.name==attr][0]
                return self.operation_wrapper

            def operation_wrapper(self, kwargs):
                data_types = dict()
                for t in [ts for ts in self.definition.types]:
                    for s in [sc for sc in t.schemas]:
                        for e in [el for el in s.elements]:
                            if self.operation.input.name==e.name:
                                for subelm in e.subelements:
                                    for el in subelm.elements:
                                        data_types[el.get('name')] = el.get('type')
                soap_types = list()
                for key in kwargs.keys():
                    if key in data_types.keys():
                        soap_types.append( "<kcen:%s>%s</kcen:%s>" % (key,
                                                            kwargs[key],
                                                            key) )
                if 'http' in self.definition.binding.soap_binding.get('transport'):
                    transport = 'http://'
                elif 'https' in self.definition.binding.soap_binding.get('transport'):
                    transport = 'https://'
                request_url = os.path.join(transport,
                                           self.definition.service.ports[0].ext_element.get('location'),
                                           self.definition.portType.name)                        
                soap_body = """<kcen:%s>%s</kcen:%s>""" % (self.operation.input.name,
                                                           "".join(soap_types),
                                                           self.operation.input.name)
                soaprequest = SOAPRequest(request_url, http.basic(self.instance.credentials), soap_body)
                return soaprequest.send()
            
        definition = self.definitions.get(attr, None)
        # print definition.service.name
        if definition is not None:
            return WSDLo(self,
                         self.definitions.get(attr))
        else:
            emsg = "%s object has no attribute '%s'" % (self.__class__.__name__,
                                                        attr)
            raise AttributeError(emsg)

            
