"""
redislog - a redis logging handler for python

>>> from redislog import handlers, logger
>>> l = logger.RedisLogger('my.logger')
>>> l.addHandler(handlers.RedisHandler.to("my:channel"))
>>> l.info("I like pie!")
>>> l.error("Oh snap", exc_info=True)

Redis clients subscribed to my:channel will get a json log record.

On errors, if exc_info is True, a printed traceback will be included.
"""

__author__ = 'Jed Parsons <jed@jedparsons.com>'
__version__ = (0, 0, 1)

import logging
import logger

logging.setLoggerClass(logger.RedisLogger)


