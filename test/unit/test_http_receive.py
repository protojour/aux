from unittest2 import TestCase
from aux.protocol.http.http import HTTP
import struct
import os

class FakeTransport(object):

    def __init__(self, message):
        self.fake_message = message
        self.bytes_read = 0
        
    def recv(self, nofchar=1200):
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


class HTTPReceiveTest(TestCase):

    def test_receive_200_startline_only(self):
        message = "HTTP/1.1 200 OK\r\n"
        http = HTTP()
        response = http.receive(FakeTransport(message))
        self.assertEquals(response.status,
                          200)

    def test_receive_200_only_headers(self):
        message = """HTTP/1.1 200 OK\r\nServer: nginx/1.5.13\r\nDate: Sat, 02 Aug 2014 19:40:38 GMT\r\nContent-Type: text/html\r\nContent-Length: 0\r\nLast-Modified: Mon, 14 Apr 2014 08:38:26 GMT\r\nConnection: keep-alive\r\nExpires: Sat, 02 Aug 2014 20:40:38 GMT\r\nCache-Control: max-age=3600\r\nAccept-Ranges: bytes\r\n\r\n"""
        http = HTTP()
        response = http.receive(FakeTransport(message))
        self.assertEquals(len(response.body), 0)
        self.assertEquals(len(response.headers), 9)
                          
    def test_receive_200_with_json_body(self):
        message = """HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: 15\r\n\r\n{{Hello:world}}"""
        http = HTTP()
        response = http.receive(FakeTransport(message))
        self.assertEqual(len(response.body), 15)

    def test_receive_200_with_long_body(self):
        data_length = 1664
        data = "".join(['ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i%26] for i in xrange(0, data_length)])
        message = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: %i\r\n\r\n%s""" % (data_length, data)
        http = HTTP()
        response = http.receive(FakeTransport(message))
        self.assertEqual(len(response.body), data_length)
        
    def test_receive_200_with_chunked_no_body(self):
        message = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nTransfer-Encoding : chunked\r\n\r\n0\r\n\r\n0"""
        http = HTTP()
        response = http.receive(FakeTransport(message))
        self.assertEqual(len(response.body), 0)

    def test_receive_200_with_chunked_no_body_one_terminating_zero(self):
        message = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nTransfer-Encoding : chunked\r\n\r\n0"""
        http = HTTP()
        response = http.receive(FakeTransport(message))
        self.assertEqual(len(response.body), 0)


    def test_receive_200_with_chunked_body_one_terminating_zero(self):
        content = '{"status":400,"code":"Client.UserInputException","message":"No content to map due to end-of-input\n at [Source: org.apache.catalina.connector.CoyoteInputStream@3d820d7f; line: 1, column: 1]"}'
        message = '''HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nTransfer-Encoding : chunked\r\n\r\n%s\r\n%s\r\n
0''' % (hex(len(content))[2:], content)
        http = HTTP()
        response = http.receive(FakeTransport(message))
        self.assertEqual(len( repr(response.body)[1:-1] ), len(repr(content)[1:-1]))
        self.assertEqual(response.body,
                         content)
        
    def test_receive_200_with_chunked_body(self):
        content = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
        message = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nTransfer-Encoding : chunked\r\n\r\n1a\r\n%s\r\n0\r\n\r\n0""" % content
        http = HTTP()
        response = http.receive(FakeTransport(message))
        self.assertEqual(len(response.body), 26)
        self.assertEqual(len(response.body), len(content))
        self.assertEqual(response.body, content)

    def xtest_receive_200_with_chunked_multi_body(self):
        message = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nTransfer-Encoding : chunked\r\n\r\n1a\r\nABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n0\r\n\r\n0"""
        http = HTTP()
        response = http.receive(FakeTransport(message))
        self.assertEqual(len(response.body), 234)

    def xtest_receive_200_with_chunked_long_body(self):
        message = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nTransfer-Encoding : chunked\r\n\r\n1a\r\nABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n34\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\nd0\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\nd0\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\nd0\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\nd0\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\nd0\r\nABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ\r\n0\r\n\r\n0"""
        http = HTTP()
        response = http.receive(FakeTransport(message))
        self.assertEqual(len(response.body), 1742)

    def xtest_receive_200_with_chunked_long_body(self):
        data_length = 4096
        data = "".join(['ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i%26] for i in xrange(0, data_length)])

        message = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nTransfer-Encoding : chunked\r\n\r\n%s\r\n%s\r\n%s\r\n%s\r\n0\r\n\r\n0""" % (hex(data_length)[2:] ,data, hex(data_length)[2:] ,data)
        http = HTTP()
        response = http.receive(FakeTransport(message))
        self.assertEqual(len(response.body), data_length*2)
        
    def xtest_receive_200_with_chunked_binary_body(self):
        byte_range = 256
        data = "".join([struct.pack('B', i) for i in xrange(0,byte_range)])
        message = """HTTP/1.1 200 OK\r\nContent-Type: application/zip;charset=UTF-8\r\nTransfer-Encoding : chunked\r\nContent-Disposition : attachment; filename="test_chunkbin.zip"\r\n\r\n100\r\n%s\r\n0\r\n\r\n0""" % data
        http = HTTP()
        response = http.receive(FakeTransport(message))
        self.assertEqual(response.body, "/tmp/aux/test_chunkbin.zip")
        self.assertTrue(os.path.exists(response.body))
        self.assertEqual(os.path.getsize(response.body), byte_range)
        
        

