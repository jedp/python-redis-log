=====================================================
RedisLog - A Redis Pub/Sub Logging Handler for Python
=====================================================

A logging handler for Python that publishes log messages using redis's 
pub/sub system.  You can use this to read or respond to streaming log
data in real time.

Installation
------------

The current stable release ::

    easy_install python-redis-log

The latest from github_ ::

    git clone git://github.com/jedp/python-redis-log.git
    cd python-redis-log
    python setup.py build
    python setup.py install --prefix=$HOME  # for example

.. _github: https://github.com/jedp/python-redis-log
    
Requirements
------------

- redis_ 
- The `Python redis client`_ by Andy McCurdy
- simplejson_ 

.. _redis: http://redis.io/
.. _Python redis client: https://github.com/andymccurdy/redis-py
.. _simplejson: https://github.com/simplejson/simplejson

Usage
-----

::

    >>> from redislog import handlers, logger
    >>> l = logger.RedisLogger('my.logger')
    >>> l.addHandler(handlers.RedisHandler.to("my:channel"))
    >>> l.info("I like pie")
    >>> l.error("Trousers!", exc_info=True)

Redis clients subscribed to ``my:channel`` will get a json log record like the
following (sent from function ``foo()`` in file ``test.py``: ::

    { username: 'jed',
      args: [],
      name: 'my.logger',
      level: 'info',
      line_no: 6,
      traceback: null,
      filename: 'test.py',
      time: '2011-06-02T14:50:08.237052',
      msg: 'winning',
      funcname: 'foo',
      hostname: 'smoothie.local' }

If an exception is raised, and ``exc_info`` is ``True``, the log will include
a formatted traceback in ``traceback``.

The date is stored as an ISO 8601 string in GMT.  

You can use the ``redis-cli`` shell that comes with ``redis`` to test this.  At
the shell prompt, type ``subscribe my:channel`` (replacing with the channel
name you choose, of course).  You will see subsequent log data printed in the
shell.

Serving Suggestion
------------------

Redis pub/sub messages are not persistent; they are just messages.  So you will
probably wish to use this handler in conjunction with other handlers that
actually save your data, like the standard python FileHandlers, or 
Andrei Savu's `MongoDB logging handler`_.

.. _MongoDB logging handler: https://github.com/andreisavu/mongodb-log

Contributors
------------

- `Yannis Leidel`_

.. _Yannis Leidel: http://github.com/jezdez


