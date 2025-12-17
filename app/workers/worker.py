import asyncio
import json
from app.core.redis_client import dequeue_notification
from app.schemas import NotificationRequest
from app.services.dispatch import DispatchService


async def run_worker():
    print("Worker started...")

    dispatcher = DispatchService()

    while True:
        job = await dequeue_notification(timeout=5)

        # ✅ NOTHING IN QUEUE
        if job is None:
            continue

        queue_name, payload = job
        print("Dequeued job:", payload)

        data = json.loads(payload)
        notification = NotificationRequest(**data)

        await dispatcher.dispatch(notification)


if __name__ == "__main__":
    asyncio.run(run_worker())
