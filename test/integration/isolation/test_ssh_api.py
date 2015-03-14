from unittest2 import TestCase
from aux.api import ssh


class SSH_API_Test(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def xtest_http_get(self):
        connection = ssh.connect('192.168.1.53',
                                 username='un',
                                 password='pw')

        response = connection.cmd("ls .")
        print response


        
