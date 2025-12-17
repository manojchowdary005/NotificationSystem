from fastapi import FastAPI
from app.schemas import NotificationRequest
from app.core.redis_client import enqueue_notification
from dotenv import load_dotenv
load_dotenv() 

app = FastAPI()

@app.post("/send", status_code=202)
async def send(req: NotificationRequest):
    await enqueue_notification(req.model_dump())
    return {"status": "queued"}