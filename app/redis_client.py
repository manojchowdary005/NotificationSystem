import json
from redis.asyncio import Redis

REDIS_URL = os.getenv('REDIS_URL', "redis://localhost:6379/0")

redis = Redis.from_url(REDIS_URL, decode_responses = True)

QUEUE_NAME = "notification_queue"

async def enque_notification(payload: dict):
    await redis.lpush(QUEUE_NAME, json.dumps(payload))

async def deque_notification(timeout: int = 0):
    await redis.brpop(QUEUE_NAME, timeout=timeout)