import os
import re

#TODO: use mimeparse but keep factory pattern

class DefaultController(object):

    def __init__(self, disposition, raw_body):
        self.data = raw_body

    def handle(self):
        return self.data

    
class ZIPController(object):

    def __init__(self, disposition, raw_body):
        self.disposition = disposition
        self.data = raw_body

    def handle(self):
        re_filename = re.compile(r'attachment;\s?filename="(.*\.zip)"')
        tmp_dir = "/tmp/aux"
        filename = re_filename.findall(self.disposition)[0]
        filepath = os.path.join(tmp_dir, filename)
        if not os.path.exists(tmp_dir):
            os.mkdir(tmp_dir)
        fp = open(filepath, 'w')
        fp.write(self.data)
        fp.close()
        return filepath


def mimeFactory(headers):
    content_type = headers.get('Content-Type', None)
    if content_type != None:
        if 'application/zip' in content_type:
            return ZIPController
    return DefaultController
