import logging
import redis
import simplejson as json


class RedisFormatter(logging.Formatter):
    def format(self, record):
        """
        JSON-encode a record for serializing through redis.

        Convert date to iso format, and stringify any exceptions.
        """
        data = record._raw.copy()

        # serialize the datetime date as utc string
        data['time'] = data['time'].isoformat()

        # stringify exception data
        if data.get('traceback'):
            data['traceback'] = self.formatException(data['traceback'])

        return json.dumps(data)


class RedisHandler(logging.Handler):
    """
    Publish messages to redis channel.

    As a convenience, the classmethod to() can be used as a
    constructor, just as in Andrei Savu's mongodb-log handler.
    """

    @classmethod
    def to(cklass, channel, host='localhost', port=6379, password=None, level=logging.NOTSET):
        return cklass(channel, redis.Redis(host=host, port=port, password=password), level=level)

    def __init__(self, channel, redis_client, level=logging.NOTSET):
        """
        Create a new logger for the given channel and redis_client.
        """
        logging.Handler.__init__(self, level)
        self.channel = channel
        self.redis_client = redis_client
        self.formatter = RedisFormatter()

    def emit(self, record):
        """
        Publish record to redis logging channel
        """
        try:
            self.redis_client.publish(self.channel, self.format(record))
        except redis.RedisError:
            pass


class RedisListHandler(logging.Handler):
    """
    Publish messages to redis a redis list.

    As a convenience, the classmethod to() can be used as a
    constructor, just as in Andrei Savu's mongodb-log handler.

    If max_messages is set, trim the list to this many items.
    """

    @classmethod
    def to(cklass, key, max_messages=None, host='localhost', port=6379, level=logging.NOTSET):
        return cklass(key, max_messages, redis.Redis(host=host, port=port), level=level)

    def __init__(self, key, max_messages, redis_client, level=logging.NOTSET):
        """
        Create a new logger for the given key and redis_client.
        """
        logging.Handler.__init__(self, level)
        self.key = key
        self.redis_client = redis_client
        self.formatter = RedisFormatter()
        self.max_messages = max_messages

    def emit(self, record):
        """
        Publish record to redis logging list
        """
        try:
            if self.max_messages:
                p = self.redis_client.pipeline()
                p.rpush(self.key, self.format(record))
                p.ltrim(self.key, -self.max_messages, -1)
                p.execute()
            else:
                self.redis_client.rpush(self.key, self.format(record))
        except redis.RedisError:
            pass
