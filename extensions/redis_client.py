import redis
from flask import current_app

def get_redis():
    return redis.Redis(
        host=current_app.config['REDIS_HOST'],
        port=current_app.config['REDIS_PORT'],
        decode_responses=True
    )
