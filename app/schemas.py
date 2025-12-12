from pydantic import BaseModel, Field
from typing import Literal, Optional, Dict

class NotificationRequest(BaseModel):
    type: Literal["email", "sms", "push"]
    to: str
    subject: Optional[str] = None
    message: str
    metadata: Dict = Field(default_facotry=dict)
    