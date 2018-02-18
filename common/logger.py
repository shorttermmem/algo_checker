import logging as log
import os
import sys

"""
log.INFO
log.DEBUG
log.WARNING
log.ERROR
log.CRITICAL
"""
if os.environ['_DEBUG'] == 'True':
    log_level = log.DEBUG
else:
    log_level = log.INFO

log.basicConfig(stream=sys.stderr, level=log_level)


def test_case_decorator(func):
    def func_wrapper(self):
        log.info("====== " + self.__class__.__name__ + " :: " + func.__name__ + " ======")
        func(self)
        log.info("Done " + func.__name__ + "\n")
    return func_wrapper


"""
def test_class_decorator(cls):
    class class_wrapper(object):
        def __enter__(self):
            log.info("\nEnter === === ===" + self.__class__.__name__ + "=== === ===")
            super(self)

        def __exit__(self):
            log.info("Exit ^^^ ^^^ ^^^" + self.__class__.__name__ + "^^^ ^^^ ^^^\n")
            super(self)
    return class_wrapper
"""