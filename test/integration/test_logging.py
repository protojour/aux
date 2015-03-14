from unittest2 import TestCase
import aux.logging as log


class LoggingTest(TestCase):

    def test_start_logging(self):
        log.start()

        log.info("This is a info message.")
        log.debug("This is a debug message.")
        log.error("This is an error message.")
        log.warning("This is a warning message.")
        log.critical("This is a critical message.")
