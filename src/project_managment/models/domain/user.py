from sqlalchemy import Column, String, Boolean
from sqlalchemy.sql.schema import ForeignKey
from project_managment.db import Base
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    worker_id = Column(UUID(as_uuid=True), ForeignKey('workers.id'))
