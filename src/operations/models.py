from datetime import datetime
from sqlalchemy import TIMESTAMP, Column, Integer, String, Table, ForeignKey
from src.database import metadata
from src.database import Client as user # ??????????

# message = Table(
#     "message",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String, nullable=False),
#     Column("dt", TIMESTAMP, default=datetime.utcnow),
#     Column("id_user", Integer, ForeignKey(user.c.id)),
# )

from sqlalchemy import Column, Integer, String

from src.database import Base


class message(Base):
    __tablename__ = "message"
    __table_args__ = {'extend_existing': True, 'schema': 'public'}
    metadata = metadata

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    dt = Column(TIMESTAMP, default=datetime.utcnow())
    id_user = Column(Integer, ForeignKey(user.id))
