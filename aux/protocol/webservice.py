from aux.protocol.soap.wsdl import WSDLDefinitions
from aux.api import http
from lxml import etree
import os


class WebServiceNotFoundError(Exception):pass


class WebService(object):

    def __init__(self, source, client):
        self.source = source
        self.client = client
        # print self.source


class WSDLService(WebService):

    def __init__(self, source, client):
        super(WSDLService, self).__init__(source, client)
        wsdl_response = http.get(self.client.get_proxy(self.source),
                                 headers=self.client.headers)
        # print wsdl_response.body
        resource = etree.XML(wsdl_response.body)
        self.definitions = WSDLDefinitions(resource)
        # print "source", self.source
        
    @classmethod
    def get_ns(cls, elmenet, namepspace):
        return '{%s}' % element.nsmap.get(namespace) if element.nsmap.get(namespace) else '{%s}' % element.nsmap.get(None)
        
        
class RESTService(WebService):
    
    def __init__(self, source, client):
        super(RESTService, self).__init__(source, client)        


def webservice_factory(source, client):
    if source.endswith('.wsdl'):
        return WSDLService(source, client)
    elif source.endswith('.json'):
        return RESTService(source, client)
    raise WebServiceNotFoundError("No handler for %s" % source)
    

class WSClient(object):

    def __init__(self, service):
        self.service = service
        self.__api_sources = list()
        self.webservices = dict()
        self.prefix = self.service.PREFIX
        self.SCHEME = self.service.get_scheme        
        self.headers = {'Host':self.service.hostname,
                        'User-Agent': 'Aux/0.1 (X11;Ubuntu;Linux x86_64;rv:24.0)',
                        'Accept':'*/*'}        


    def get_proxy(self, path, prefix=None):
        if prefix == None:
            prefix = self.prefix
        return "%s%s%s%s" % (self.SCHEME(),
                             self.service.hostname,
                             prefix,
                             path)
    
    def set_api_source(self, new_api_source_dsn):
        self.__api_sources.append(new_api_source_dsn)

    def get_api_sources(self):
        return self.__api_sources

    def update_api(self):
        try:
            for source in self.get_api_sources():
                source_name = os.path.basename(source).replace('.wsdl','')
                self.webservices[source_name] = webservice_factory(source, self)
        except WebServiceNotFoundError, e:
            print e.message

    def set_credentials(self, credentials):
        self.credentials = credentials
        # self.headers.update(http.basic(self.credentials))
        # log.debug("WSDL credentials changed")

    def get_credentials(self):
        return self.credentials

    
    def __getattr__(self, attr):
        # print 'attr', attr
        definition = self.webservices.get(attr, None)
        if definition is not None:
            print definition
            return definition
        else:
            emsg = "%s object has no attribute '%s'" % (self.__class__.__name__,
                                                        attr)
            raise AttributeError(emsg)
            
        #     return WSDLo(self,
        #                  self.definitions.get(attr))
        # else:
        #     emsg = "%s object has no attribute '%s'" % (self.__class__.__name__,
        #                                                 attr)
        #     raise AttributeError(emsg)
