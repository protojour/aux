from aux.protocol.transport import TCP_DEFAULT_FRAME_SIZE
import re

class DefaultController(object):

    def __init__(self, headers, transport, msg):
        self.headers = headers
        self.transport = transport
        self.msg = msg

    def read(self):
        raw_response = self.msg
        content_length = int(self.headers.get('Content-Length', 0))
        response = ""
        while 1:
            if content_length < 1:
                break
            if content_length > len(raw_response):
                raw_response += self.transport.recv()
            response += raw_response
            content_length -= len(raw_response)
            raw_response = ""
        return response

class NoContentController(object):
    def __init__(self, headers, transport, msg):
        self.headers = headers
        self.transport = transport
        self.msg = msg

    def read(self):
        return self.msg


class ChunkedController(object):

    def __init__(self, headers, transport, msg):
        self.headers = headers
        self.transport = transport
        self.msg = msg
        
    def read(self):
        re_chunk = re.compile(r'^([a-f|\d]{1,4})\r\n')
        re_end_chunk = re.compile(r'^0\r\n\r\n0')
        re_single_end_chunk = re.compile(r'0\r\n\r\n')
        raw_response = self.msg
        response = ""
        block = 0
        chunk_cdown = 0
        i_next_chunk = 0
        while 1:
            if chunk_cdown == 0:
                next_chunk = re_chunk.findall(raw_response[0:8])
                end_chunk = re_end_chunk.findall(raw_response[0:8])
                broken_end_chunk = re_single_end_chunk.findall(raw_response[0:8])
                if len(next_chunk) > 0:
                    i_next_chunk = int(next_chunk[0], 16)
                    chunk_cdown = i_next_chunk
                    raw_response = raw_response[len(next_chunk[0])+2:]
                    if i_next_chunk == 0 or len(end_chunk) > 0:
                        break
            if len(broken_end_chunk) > 0:
                break
            if i_next_chunk > len(raw_response):
                    raw_response += self.transport.recv()
            if len(raw_response) <= 0:
                break
            block, nl_skip = (len(raw_response), 0) if len(raw_response) < chunk_cdown else (chunk_cdown, 1)
            response += raw_response[:block]
            raw_response = raw_response[block+nl_skip:]
            chunk_cdown -= block
        return response

def transferFactory(headers):
    content_length = headers.get('Content-Length', None)
    if content_length != None:
        if int(content_length) < 1:
            return NoContentController
    content_type = headers.get('Transfer-Encoding', None)
    if content_type != None:
        if 'chunked' in content_type.lower():
            return ChunkedController
    return DefaultController
