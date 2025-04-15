from pydantic import BaseModel, Field
from datetime import datetime
from uuid import uuid4

class EventPayload(BaseModel):
    username: str
    tenant: str

class EventLog(BaseModel):
    environment: str
    event_type: str
    timestamp: datetime
    trace_id: str = Field(default_factory=lambda: str(uuid4()))
    payload: str