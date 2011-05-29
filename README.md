RedisLog - A Redis Pub/Sub Logging Handler for Python
=====================================================

A logging handler for Python that publishes log messages using redis's 
pub/sub system.  You can use this to read or respond to streaming log
data in real time.

Installation
------------

Git clone this repo

Or `easy_install python-redis-log`

Requirements
------------

You will need:

- [redis](http://redis.io/)
- The Python [redis](https://github.com/andymccurdy/redis-py) client by Andy
  McCurdy
- [simplejson](https://github.com/simplejson/simplejson)

Usage
-----

    >>> from redislog import handlers, logger
    >>> l = logger.RedisLogger('my.logger')
    >>> l.addHandler(handlers.RedisHandler.to("my:channel"))
    >>> l.info("I like pie!")
    >>> l.error("Oh snap", exc_info=True)

Redis clients subscribed to `my:channel` will get a json log record.

If an exception is raised, and `exc_info` is `True`, the log will include
a formatted traceback.

Serving Suggestion
------------------

I recommend using this in conjunction with 
[Andrei Savu's MongoDB logging handler](https://github.com/andreisavu/mongodb-log),
or at least some handler that will actually save your data somewhere.




