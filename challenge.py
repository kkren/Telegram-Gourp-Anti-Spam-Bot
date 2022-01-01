import uuid
from redisInstance import redis_instance
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def new_challenge(user_id):
    session_key = str(uuid.uuid4())
    redis_instance.set(user_id, session_key)
    return session_key