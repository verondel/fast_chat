from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, Column, Integer, String, TIMESTAMP, ForeignKey, Boolean
from src.database import Base

metadata = MetaData()

class Client(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)


class Message(Base):
    __tablename__ = "message"
    # __table_args__ = {'extend_existing': True, 'schema': 'public'}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    dt = Column(TIMESTAMP, default=datetime.utcnow())
    id_user = Column(Integer, ForeignKey(Client.id))




# class User(Base, SQLAlchemyBaseUserTable):
#     __tablename__ = "client"
#     # __table_args__ = {'extend_existing': True}
#
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, nullable=False, unique=True)
#     username = Column(String, nullable=False, unique=True)
#     registered_at = Column(TIMESTAMP, default=datetime.utcnow)
#     hashed_password = Column(String, nullable=False)
#     is_active = Column(Boolean, default=True, nullable=False)
#     is_superuser = Column(Boolean, default=False, nullable=False)
#     is_verified = Column(Boolean, default=False, nullable=False)

# user = Table(
#     "user",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("email", String, nullable=False),
#     Column("username", String, nullable=False),
#     Column("registered_at", TIMESTAMP, default=datetime.utcnow),
#     Column("hashed_password", String, nullable=False),
#     Column("is_active", Boolean, default=True, nullable=False),
#     Column("is_superuser", Boolean, default=False, nullable=False),
#     Column("is_verified", Boolean, default=False, nullable=False),
# )

# message = Table(
#     "message",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String, nullable=False),
#     Column("dt", TIMESTAMP, default=datetime.utcnow),
#     Column("id_user", Integer, ForeignKey(user.c.id)),
# )
