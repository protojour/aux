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


    def consume_buffer(self, i_chunk, raw_buffer):
        print( i_chunk, len(raw_buffer) )
        return raw_buffer[:i_chunk]
    
    def read(self, has_trace=False):
        re_chunk = re.compile(r'^([a-f|\d]{1,4})')
        re_chunk_block = re.compile(r'[\r\n]{0,2}[a-f|\d]{1,4}[\r\n]{0,2}', re.DOTALL)
        re_end_chunk = re.compile(r'^0\r\n\r\n0')
        re_single_end_chunk = re.compile(r'0[\r\n]{0,2}')
        raw_response = self.msg
        response = ""
        block = 0
        chunkcounter = 0
        i_chunk = 0

        while 1:
            if chunkcounter == 0:#When chunk has been consumed
                chunk = re_chunk.findall(raw_response[0:8])
                print 'a_', re_chunk_block.findall(raw_response[0:8])
                end_chunk = re_end_chunk.findall(raw_response[0:8])
                broken_end_chunk = re_single_end_chunk.findall(raw_response[0:8])
                
                if len(chunk) > 0:
                    self.chunks_in_stream.append(chunk[0])                    
                    i_chunk = int(chunk[0], 16)
                    chunkcounter = i_chunk
                    raw_response = raw_response[len(chunk[0])+1:]
                    if i_chunk == 0 or len(end_chunk) > 0:
                        break
                    while i_chunk > len(raw_response):
                        raw_response += self.transport.recv(TCP_DEFAULT_FRAME_SIZE)
                        
            # print chunk, end_chunk, broken_end_chunk, len(raw_response), i_chunk, chunkcounter

            # if len(broken_end_chunk) > 0 or len(raw_response) <= 0:
            #     break
            # block, nl_skip = (len(raw_response), 0) if len(raw_response) < chunkcounter else (chunkcounter, 1)
            # if len(end_chunk) > 0:
            #     response += raw_response[:-len(end_chunk)-1]#if termination is detected strip termination 0
            #     break

            response += self.consume_buffer(i_chunk, raw_response)
            a = len(raw_response)
            raw_response = raw_response[i_chunk:]
            print len(raw_response), a-i_chunk
            print raw_response[0:8]
            
            # response += raw_response[:block]
            # raw_response = raw_response[block+nl_skip:]
            # chunkcounter -= block
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
