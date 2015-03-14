import paramiko


class SSHMessage(object):
    def __init__(self):
        self.packet_length
        self.padding_length
        self.payload
        self.random_padding

#RFC4253
class SSHClient(object):
    credentials = None
    
    def __init__(self):
        self.hostname = None
        self.__connection = paramiko.SSHClient()
        self.__connection.load_system_host_keys()
        self.__connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def set_hostname(self, hostname):
        self.hostname = hostname
        
    def set_credentials(self, credentials):
        self.credentials = credentials
    
    def cmd(self, command_msg):
        self.__connection.connect(self.hostname,
                                  username=self.credentials[0],
                                  password=self.credentials[1])
        stdin, stdout, stderr = self.__connection.exec_command(command_msg)
        return stdout.read()

#initial handshake

#resilliency signaling

#data (re)transmission



#[1] SSH Connection Protocol

#[2] SSH User Authentication Protocol

#[3] SSH Transport Protocol


"""
      uint32    packet_length
      byte      padding_length
      byte[n1]  payload; n1 = packet_length - padding_length - 1
      byte[n2]  random padding; n2 = padding_length
      byte[m]   mac (Message Authentication Code - MAC); m = mac_length

      packet_length
         The length of the packet in bytes, not including 'mac' or the
         'packet_length' field itself.

      padding_length
         Length of 'random padding' (bytes).

      payload
         The useful contents of the packet.  If compression has been
         negotiated, this field is compressed.  Initially, compression
         MUST be "none".

      random padding
         Arbitrary-length padding, such that the total length of
         (packet_length || padding_length || payload || random padding)
         is a multiple of the cipher block size or 8, whichever is
         larger.  There MUST be at least four bytes of padding.  The
         padding SHOULD consist of random bytes.  The maximum amount of
         padding is 255 bytes.

      mac
         Message Authentication Code.  If message authentication has
         been negotiated, this field contains the MAC bytes.  Initially,
         the MAC algorithm MUST be "none".
"""
