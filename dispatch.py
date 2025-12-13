from app.schemas import NotificationRequest
from app.email_service import send_email
from app.push_service import send_push
from app.sms_service import send_sms

class DispatchService:
    async def dispatch(self, notification: NotificationRequest):
        if notification.type == "email":
            return await send_email(notification.to, notification.subject or "", notification.message, notification.metadata)
        if notification.type == "sms":
            return await send_sms(notification.to, notification.message, notification.metadata)
        if notification.type == "push":
            return await send_push(notification.to, notification.message, notification.metadata)
        raise ValueError("Unknown type")