from aux.protocol.transport import (TCPTransport, TLS_TCPTransport, TCP_DEFAULT_FRAME_SIZE)
from urlparse import urlparse, urlunparse
from aux.protocol.http.transfer import transferFactory
from aux.protocol.http.mime import mimeFactory
import auth
import logging
import aux
import re
import os
import base64

log = logging.getLogger("protocol")

uname = os.uname()
USER_AGENT = "aux/%s (%s;)" % (aux.version(),
                              " ".join([uname[0], uname[-1]]))
CRLF = "\r\n"
HTTP_DEFAULT_PORT = 80
HTTPS_DEFAULT_PORT = 443
TCP_FRAME_BUFFER_SIZE = 1500#bytes#hmmmm
#TODO: enum wrapper
HTTP_METHODS = ["OPTIONS", "GET", "HEAD",
                "POST", "PUT", "DELETE",
                "TRACE", "CONNECT"]#extension-method
# M_GET  = 'GET'
# M_POST = 'POST'
# M_PUT  = 'PUT'
# M_DELETE  = 'DELETE'
# M_HEAD = 'HEAD'

HTTP_RESPONSE_CODES = {"100": "Continue",
                       "101": "Switching Protocols",
                       "200": "OK",
                       "201": "Created",
                       "202": "Accepted",
                       "203": "Non-Authoritative Information",
                       "204": "No Content",
                       "205": "Reset Content",
                       "206": "Partial Content",
                       "300": "Multiple Choices",
                       "301": "Moved Permanently",
                       "302": "Found",
                       "303": "See Other",
                       "304": "Not Modified",
                       "305": "Use Proxy",
                       "307": "Temporary Redirect",
                       "400": "Bad Request",
                       "401": "UnauthorizedRequest",
                       "402": "Payment Required",
                       "403": "Forbidden",
                       "404": "Not Found",
                       "405": "Method Not Allowed",
                       "406": "Not Acceptable",
                       "407": "Proxy Authentication Required",
                       "408": "Request Time-out",
                       "409": "Conflict",
                       "410": "Gone",
                       "411": "Length Required",
                       "412": "Precondition Failed",
                       "413": "Request Entity Too Large",
                       "414": "Request-URI Too Large",
                       "415": "Unsupported Media Type",
                       "416": "Requested range not satisfiable",
                       "417": "Expectation Failed",
                       "500": "Internal Server Error",
                       "501": "Not Implemented",
                       "502": "Bad Gateway",
                       "503": "Service Unavailable",
                       "504": "Gateway Time-out",
                       "505": "HTTP Version not supported"}

"""
RESPONSE_HEADER = [Accept-Ranges, Age, ETag, Location, Proxy-Authenticate, Retry-After, Server, Vary, WWW-Authenticate]

"""
"""
HTTP

Authentication Type: On Request; Preemptive; SPNEGO/Kerberos; NTLM1|2

"""

class HTTPMessage(object):
    http_version = 1.1
    target = None
    headers = dict()
    body = None

    def __init__(self, headers, body):
        self.headers = headers
        self.body = body
        
    def __str__(self):
        return CRLF.join([CRLF.join([": ".join(item) for item in self.headers.items()]),
                          "",#zero-length-http-message-line
                          self.body])

class HTTPRequest(HTTPMessage):
    url = None
    def __init__(self, url, request_data={}):       
        self.method = request_data.get('method', 'GET').upper()
        self.url = urlparse(url)
        if len(self.url.path) == 0:
            l = list(self.url)
            l[2] = l[2] + "/"
            self.url = urlparse(urlunparse(l))
        headers = {'Host': self.url.hostname,
                   'User-Agent': USER_AGENT}
        headers.update(request_data.get('headers', {}))
        super(HTTPRequest, self).__init__(headers,
                                          request_data.get('body', ''))

    def __str__(self):
        return CRLF.join(["%s %s HTTP/%0.1f" % (self.method, self.url.path, self.http_version),
                          super(HTTPRequest, self).__str__()])

    
class HTTPResponse(HTTPMessage):
    def __init__(self, status, response_data={}, request_pointer=None):
        self.status = status
        self.request_pointer = request_pointer
        super(HTTPResponse, self).__init__(response_data.get('headers', {}),
                                           response_data.get('body', ''))
        
    def __str__(self):
        return CRLF.join(["HTTP/%0.1f %s %s" % (self.http_version, self.status, HTTP_RESPONSE_CODES[str(self.status)]),
                          super(HTTPResponse, self).__str__()])
    


class HTTP(object):
    __is_persistent = False
    __has_trace = False
    
    def __init__(self):
        self.logger = logging.getLogger('protocol')
        self._transport = None
   
    def get_transport(self, url, scheme="http", persist=False, timeout=60):
        # if self._transport != None and persist:
        #     return self._transport
        #TODO: ternary default port assign is a bad idea as traceability is lost in request update url instead
        transport = None
        if "https" == scheme.lower():
            transport = TLS_TCPTransport(url.hostname,
                                         443 if url.port == None else int(url.port),
                                         timeout=timeout)
        else:
            transport = TCPTransport(url.hostname,
                                     80 if url.port == None else int(url.port),
                                     timeout=timeout)
        transport.connect()
        self.logger.debug('Connected to %s:%s' % (transport.addr[0],
                                                  transport.addr[1]))
        return transport
    
    def is_persistent(self):
        return self.__is_persistent

    def has_trace(self, should_trace=None):
        if should_trace is not None:
            self.__has_trace = should_trace
        return self.__has_trace
    
    def set_url_from_string(self, raw_url):
        url = urlparse(raw_url)
        if not url.port:
            l = list(url)
            l[1] = l[1] + ":%i" % HTTP_DEFAULT_PORT
            url = urlparse(urlunparse(l))        
        return url

    def receive(self, transport):
        #TODO: this impl needs TLC
        inbuf = transport.recv(TCP_DEFAULT_FRAME_SIZE)
        inbuf = inbuf.split("\n")
        # inbuf = transport.recv_all()
        sl = inbuf[0]
        #Validate start-line and remove it from buffer
        re_startline = re.compile(r'^HTTP\/\d\.\d\s(\d{3})\s')
        tail_msg = "\n".join(inbuf[1:])
        try:
            status = int(re_startline.match(sl).groups()[0])
        except Exception, e:
            log.error(e.message)
            raise Exception

        re_headline = re.compile(r'^([A-Za-z\-]*)\s?\:\s?(.*)')
        headers = dict()
        body = ""
        t_lines = tail_msg.split("\r\n\r\n")
        if len(t_lines) == 1: #Servers can respond with \r\n or \n
            t_lines = tail_msg.split("\n\n")
        h_lines = t_lines[0].split("\n")
        line_counter = 0
        for line in h_lines:
            line_counter += 1
            if ":" in line:
                re_group = re_headline.match(line).groups()
                headers[re_group[0]] = re_group[1]
            else:
                break
        tail_msg = tail_msg[len(t_lines[0]):]
        # if self.__has_trace:
        #     print tail_msg
        log.debug(headers)
        Transfer = transferFactory(headers)
        Mime = mimeFactory(headers)
        body = Mime(headers.get('Content-Disposition', None),
                    Transfer(headers, transport, tail_msg).read()).handle()
        response = HTTPResponse(status, {'headers': headers, 'body': body})
        log.debug("mime : %s\ntrans : %s" % (Mime, Transfer))        
        # log.debug("HTTPResponse:\n%s\n", response)
        transport.close()
        return response
    
    def send(self, request):
        request.target = request.url.hostname
        if request.method in ['POST', 'PUT', 'DELETE']:
            request.headers.update({'Content-Length': '%i' % len(request.body)})
        transport = self.get_transport(request.url, scheme=request.url.scheme)
        log.debug("HTTPRequest:\n%s\n", request)
        transport.send(str(request))
        response = self.receive(transport)
        response.request_pointer = request
        return response

class HTTPScheme(object):
    scheme = "http://"
    
    def __call__(self, scheme):
        self.scheme = scheme

    def __repr__(self):
        return self.scheme
    
class HTTPClient(object):
    auth = auth
    __has_trace = False
    scheme = HTTPScheme()
    
    def has_trace(self, should_trace=None):
        if should_trace is not None:
            self.__has_trace = should_trace
        return self.__has_trace
    
    def http_send(self, method, url, headers, body, request):
        if request == None:
            request = HTTPRequest(url,
                                  {'method': method,
                                   'headers': headers,
                                   'body': body})
        _http = HTTP()
        _http.has_trace(self.__has_trace)
        return _http.send(request)

    def head(self, url=None, headers={}, request=None):
        return self.http_send('HEAD', url, headers, "", request)
    
    def get(self, url=None, headers={}, body="", request=None):
        return self.http_send('GET', url, headers, body, request)

    def post(self, url, headers={}, body="", request=None):
        return self.http_send('POST', url, headers, body, request)

    def put(self, url, headers={}, body="", request=None):
        return self.http_send('PUT', url, headers, body, request)

    def patch(self, url, headers={}, body="", request=None):
        return self.http_send('PATCH', url, headers, body, request)
        
    def delete(self, url, headers={}, body="", request=None):
        return self.http_send('DELETE', url, headers, body, request)

    def connect(self, url, headers={}, body="", request=None):
        return self.http_send('CONNECT', url, headers, body, request)

    def trace(self, url, headers={}, body="", request=None):
        return self.http_send('TRACE', url, headers, body, request)    

    def options(self, url, headers={}, body="", request=None):
        return self.http_send('OPTIONS', url, headers, body, request)    

    def basic(self, credentials):
        return {'Authorization': 'Basic %s' % base64.b64encode(
                '%s:%s' % (credentials[0],
                           credentials[1]))}
