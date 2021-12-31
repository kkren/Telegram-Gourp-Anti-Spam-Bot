import uuid
from redisInstance import redis_instance

class Challenge:
    def new_challenge(uid):
        session_key = str(uuid.uuid4())
        user_id = uid
        redis_instance.set(session_key, user_id)

