from datetime import datetime
from pydantic import BaseModel


class MessagesModel(BaseModel):
    id: int
    name: str
    dt: datetime
    id_user: int

    class Config:
        orm_mode = True
