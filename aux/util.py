from colorama import Fore, Back, Style
import os
import logging
from aux import logcontroller

def as_role(method):
    return method

def as_user(method):
    return method


def expected(expected_result,
             actual_result,
             service="",
             note=None,
             error_msg=None):
    log = logging.getLogger('script')

    if actual_result != expected_result:
        # color_s = Fore.RED + "Error: %s" + Fore.RESET
        color_s = " Err: %s"
        log.error(color_s % service)
        log.error(" Actual:%s != %s:Expected" % (actual_result, expected_result))
        logcontroller.summary['success'] = False        
        if note is not None:
            log.info("   : %s" % (note))
        if error_msg is not None:
            log.error("   : %s" % (error_msg))
    else:
        # color_s = Fore.GREEN + "OK: %s" + Fore.RESET
        color_s = " OK : %s"
        log.info(color_s % service)
        if note is not None:
            log.info("   : %s" % (note))
