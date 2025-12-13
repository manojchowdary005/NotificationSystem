from fastapi import FastAPI
from app.schemas import NotificationRequest
from app.core.redis_client import enque_notification

app = FastAPI()

@app.post("/send", status_code=202)
async def send(req: NotificationRequest):
    await enque_notification(req.model_dump())
    return {"status": "queued"}