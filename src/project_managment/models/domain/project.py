from sqlalchemy import Column, String, Boolean, Date
from db import Base
from sqlalchemy.orm import relationship
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from .association import worker_project
import datetime

class Project(Base):
    __tablename__ = 'projects'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    start_date = Column(Date, nullable=False, default=datetime.datetime.now(), index=True)
    end_date = Column(Date, nullable=False, index=True)
    workers = relationship('Worker', secondary=worker_project, backref='projects')