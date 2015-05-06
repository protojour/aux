from aux.protocol.transport import TCP_DEFAULT_FRAME_SIZE
import re


class NoContentController(object):
    def __init__(self, headers, transport, msg):
        self.headers = headers
        self.transport = transport
        self.msg = msg.lstrip()

    def read(self):
        return self.msg.rstrip()


class DefaultController(NoContentController):

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
        return response.rstrip()


class ChunkedController(NoContentController):

    chunks_in_stream = list()
        
    def read(self, has_trace=False):
        re_chunk = re.compile(r'^([a-f|\d]{1,4})')
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
                self.chunks_in_stream.append(next_chunk)
                end_chunk = re_end_chunk.findall(raw_response[0:8])
                broken_end_chunk = re_single_end_chunk.findall(raw_response[0:8])
                if len(next_chunk) > 0:
                    i_next_chunk = int(next_chunk[0], 16)
                    chunk_cdown = i_next_chunk
                    raw_response = raw_response[len(next_chunk[0])+2:]
                    if i_next_chunk == 0 or len(end_chunk) > 0:
                        break
            # print next_chunk, end_chunk, broken_end_chunk, i_next_chunk, chunk_cdown
            if len(broken_end_chunk) > 0:
                break
            if i_next_chunk > len(raw_response):
                raw_response += self.transport.recv(TCP_DEFAULT_FRAME_SIZE)
            if len(raw_response) <= 0:
                break
            block, nl_skip = (len(raw_response), 0) if len(raw_response) < chunk_cdown else (chunk_cdown, 1)
            response += raw_response[:block]
            raw_response = raw_response[block+nl_skip:]
            chunk_cdown -= block
        print("->",self.chunks_in_stream,"<-")
        return response

class ALTChunkedController(NoContentController):

    chunks_in_stream = list()
        
    def read(self, has_trace=False):
        re_chunk = re.compile(r'^([a-f|\d]{1,4})')
        re_end_chunk = re.compile(r'^0\r\n\r\n0')
        re_single_end_chunk = re.compile(r'0\r\n\r\n')
        raw_response = self.msg
        response = ""
        block = 0
        chunk_cdown = 0
        i_next_chunk = 0

        while 1:
            if chunk_cdown == 0:#When chunk has been consumed

                #identify chunks in available raw_response part
                next_chunk = re_chunk.findall(raw_response[0:8])
                end_chunk = re_end_chunk.findall(raw_response[0:8])
                broken_end_chunk = re_single_end_chunk.findall(raw_response[0:8])
                
                if len(next_chunk) > 0:
                    self.chunks_in_stream.append(next_chunk[0])                    
                    i_next_chunk = int(next_chunk[0], 16)
                    chunk_cdown = i_next_chunk
                    print "[%s]" % raw_response[len(next_chunk[0]):16].lstrip()
                    raw_response = raw_response[len(next_chunk[0]):].lstrip()
                    
                    if i_next_chunk == 0 or len(end_chunk) > 0:
                        break

            print next_chunk, end_chunk, broken_end_chunk, i_next_chunk, chunk_cdown
                    
            if i_next_chunk > len(raw_response):
                raw_response += self.transport.recv(TCP_DEFAULT_FRAME_SIZE)
            if len(broken_end_chunk) > 0 or len(raw_response) <= 0:
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
            return ALTChunkedController
    return DefaultController
