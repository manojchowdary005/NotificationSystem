from pydantic import BaseModel, Field
from typing import Literal, Optional, Dict, Any

class NotificationRequest(BaseModel):
    type: Literal["email", "sms", "push"]
    to: str
    subject: Optional[str] = None
    message: str
    metadata: Dict[str, Any] = Field(default_factory=dict)