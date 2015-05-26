from unittest2 import TestCase
from urlparse import urlparse
from aux.protocol.transport import TCPTransport, UDPTransport

from socket import (AF_INET, SOCK_DGRAM, SOL_SOCKET,
                    SO_REUSEADDR)                                         
from multiprocessing import Process
import socket
import time


class MockUDPServer(object):
    def __init__(self, port=8989):
        self.port = port
        self.host = '127.0.0.1'
        self.__socket = socket.socket(AF_INET, SOCK_DGRAM)
        self.__socket.bind((self.host, self.port))

    def start(self):
        # print "starting", self.__class__.__name__
        while True:
            d, addr = self.__socket.recvfrom(2048)
            self.__socket.sendto('response connection', addr)

    def start_thread(self):
        self.p = Process(target=self.start)
        self.p.daemon = True
        self.p.start()
        time.sleep(.01)

    def stop(self):
        self.p.terminate()
        self.__socket.close()
        
class MockTCPServer(object):
    def __init__(self, port=8989):
        self.port = port
        self.host = '127.0.0.1'#socket.gethostname()
        self.__socket = socket.socket()
        self.__socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.__socket.bind((self.host, self.port))
        
    
    def start(self):
        # print "starting", self.__class__.__name__
        self.__socket.listen(5)
        while True:
            c, addr = self.__socket.accept()
            c.send('response connection')
            c.close()

    def start_thread(self):
        self.p = Process(target=self.start)
        self.p.daemon = True
        self.p.start()
        time.sleep(.5)

    def stop(self):
        self.p.terminate()
        self.__socket.close()
        

class TCPTransportTest(TestCase):
    
    def setUp(self):
        self.test_server = MockTCPServer(port=8989)
        self.test_server.start_thread()

    def tearDown(self):
        self.test_server.stop()
        
    def test_connection(self):
        conn = TCPTransport('127.0.0.1', 8989)
        conn.connect()
        conn.send("hello world: END\n")
        data = conn.recv()
        self.assertEquals('response connection',
                          data)
        conn.close()
        

class UDPConnectionTest(TestCase):

    def setUp(self):
        self.test_server = MockUDPServer(port=8888)
        self.test_server.start_thread()

    def tearDown(self):
        self.test_server.stop()

    def test_connection(self):
        conn = UDPTransport('127.0.0.1', 8888)
        conn.connect()
        conn.send("hello world UDP: END\n")
        data = conn.recv()
        self.assertEquals('response connection',
                          data)
        conn.close()
