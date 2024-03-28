from sqlalchemy import Column, String, Boolean,Enum
from project_managment.db import Base
from sqlalchemy.orm import relationship
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from association import worker_skill, worker_project
class RoleEnum(Enum):
    ADMIN = 'admin'
    CLIENT = 'client'
    PROJECT_MANAGER = 'project_manager'
    WORKER = 'worker'
class Worker(Base):
    __tablename__ = 'workers'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    role = Column(Enum(RoleEnum), default=RoleEnum.USER)
    location = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_available = Column(Boolean, default=True)
    user = relationship('User', backref='worker', uselist=False)
    skills = relationship('Skill', secondary=worker_skill, backref='workers')
    projects = relationship('Project', secondary=worker_project, backref='workers')