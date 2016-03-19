import redis
from gb_server import RedisHelp

obj = RedisHelp()
redis_sub = obj.subscribe()

while True:
    msg = redis_sub.parse_response()
    print(msg)