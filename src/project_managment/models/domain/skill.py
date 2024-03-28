from sqlalchemy import Column, String
from project_managment.db import Base
from sqlalchemy.orm import relationship
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from association import worker_skill

class Skill(Base):
    __tablename__ = 'skills'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False, unique=True)
    workers = relationship('Worker', secondary=worker_skill, backref='skills')