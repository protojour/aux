from unittest2 import TestCase
from aux.engine import Engine
import time

class EngineTest(TestCase):

    def setUp(self):
        self.test_engine = Engine()

    def tearDown(self):
        del self.test_engine
    
    def xtest_start_stop_engine(self):
        self.assertFalse(self.test_engine.is_running() )
        self.test_engine.start()
        self.assertTrue(self.test_engine.is_running() )
        # time.sleep(2)
        self.test_engine.stop()
        self.assertFalse(self.test_engine.is_running() )
        


