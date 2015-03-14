from urlparse import urlparse
from aux.api import http


class SOAPRequest(object):

    def __init__(self, url, headers, soap_content):
        self.url = url
        self.soap_ns = 'soapenv'
        self.headers = headers
        # self.soap_headers = soap_headers
        self.soap_content = soap_content
        self.body = self._request()

    def __str__(self):
        return self._request()
        
    def _request(self):
        return """<%s:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:kcen="http://kezzlerssp.com/schemas/kcengine" xmlns:com="http://kezzlerssp.com/schemas/common">
<%s:Header/>
<%s:Body>
%s
</%s:Body>
</%s:Envelope>""" % (self.soap_ns,
                     self.soap_ns,
                     self.soap_ns,
                     self.soap_content,
                     self.soap_ns,
                     self.soap_ns)

    def send(self):
        response = http.post(self.url,
                             headers=self.headers,
                             body=self.body)
        return SOAPResponse(http_response=response)

    
class SOAPResponse(object):

    def __init__(self, http_response=None):
        if http_response is not None:
            self.http_response = http_response
        self.body = self.soap2json(self.http_response.body)

    def soap2json(self, xml):
        # print xml
        
        return xml
        
    def __str__(self):
        return self.http_response.body


    

# class SOAP(object):

#     def __init__(self):
#         pass

#     def send(self, request):
#         return SOAPResponse(http.post(self.url,
#                                       header=self.headers,
#                                       body=self.body))



# request = '''
# POST https://aux.protojour.com/ws/test-ws HTTP/1.1
# Accept-Encoding: gzip,deflate
# Content-Type: text/xml;charset=UTF-8
# SOAPAction: ""
# Authorization: Basic abcdefghijklmnopqrstuvwx
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

# response = '''
# HTTP/1.1 200 OK
# Server: nginx/1.5.4
# Date: Wed, 12 Feb 2014 09:58:13 GMT
# Content-Type: text/xml;charset=utf-8
# Content-Length: 4734
# Connection: keep-alive
# Set-Cookie: JSESSIONID=oijoij6E0C7479C4CF531A5842241F47; Path=/; HttpOnly
# X-Request-Received: 1392199092003
# Accept: text/xml, text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2
# SOAPAction: ""
# X-Src-Nginx: aux.protojour.com

# <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
# <SOAP-ENV:Header/><SOAP-ENV:Body></SOAP-ENV:Body></SOAP-ENV:Envelope>
# '''
    
