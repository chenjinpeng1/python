import redis
class RedisHelp(object):

    def __init__(self):
        self.__conn=redis.Redis(host="localhost")
        self.chan_sub="27"
        self.chan_pub="28"

    def public(self,msg):
        self.__conn.publish(self.chan_pub,msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub