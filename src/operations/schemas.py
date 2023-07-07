from datetime import datetime
from pydantic import BaseModel


class MessageCreate(BaseModel):
    id: int
    text: str
    dt: datetime
    id_user: int
