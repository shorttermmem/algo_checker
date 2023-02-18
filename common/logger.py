import logging as log
import os
import sys
from dotenv import load_dotenv

"""
log.INFO
log.DEBUG
log.WARNING
log.ERROR
log.CRITICAL
"""

load_dotenv()

if os.getenv('_DEBUG') == 'True':
    log_level = log.DEBUG
else:
    log_level = log.INFO

log.basicConfig(stream=sys.stderr, level=log_level)
