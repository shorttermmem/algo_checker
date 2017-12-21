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
