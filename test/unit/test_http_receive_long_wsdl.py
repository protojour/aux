from unittest2 import TestCase
from aux.protocol.http.http import HTTP
import struct
import os
import re
from ..data.wsdl_raw_chunked_response import chunked_message, received_wsdl_message
from aux.protocol.transport import TCP_DEFAULT_FRAME_SIZE
from aux.protocol.http.transfer import ALTChunkedController

class FakeTransport(object):

    def __init__(self, message):
        self.fake_message = message
        self.bytes_read = 0
        
    def recv(self, nofchar=1024):
        buffer = ""
        for n in xrange(0, nofchar):
            if self.bytes_read >= len(self.fake_message):
                break
            else:
                buffer += self.fake_message[self.bytes_read]
            self.bytes_read += 1
        return buffer
    
    def close(self):
        pass

class HTTP_RECEIVE_LONG_WSDL_TEST(TestCase):
    
    def test_chunked_controller(self):
        transport = FakeTransport(chunked_message)
        inbuf = transport.recv(TCP_DEFAULT_FRAME_SIZE)
        inbuf = inbuf.split("\n")
        sl = inbuf[0]
        #Validate start-line and remove it from buffer
        re_startline = re.compile(r'^HTTP\/\d\.\d\s(\d{3})\s')
        tail_msg = "\n".join(inbuf[1:])

        status = int(re_startline.match(sl).groups()[0])

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
        
        # print headers
        self.assertEquals(headers.get('Transfer-Encoding'),
                          'chunked')
        Transfer = ALTChunkedController(headers, transport, tail_msg)
        body = Transfer.read()
        self.assertNotEquals(received_wsdl_message,
                             body)
        self.assertEqual(['1f09', '2000', '2000', '2000', '2000',
                          '2000', '2000', '2000', '2000', '2000',
                          '2000', '2000', '2000', '2000', '2000',
                          '2000', '2000', '2000', '2000', '2000',
                          '2000', '2000', '2000', '2000', '2000',
                          '1000', '81', '0'],
                         Transfer.chunks_in_stream)

    def xtest_receive_long_wsdl(self):
        message = chunked_message

        http = HTTP()
        http.has_trace(True)
        response = http.receive(FakeTransport(message))
        self.assertEquals(response.status,
                          200)
        self.assertNotEquals(response.body,
                             received_wsdl_message)

