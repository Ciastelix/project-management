from enum import Enum
from sqlalchemy import Column, String, Boolean
from sqlalchemy import Enum as SQLAlchemyEnum
from db import Base
from sqlalchemy.orm import relationship
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from .association import worker_project, worker_skill


class RoleEnum(Enum):
    ADMIN = "admin"
    CLIENT = "client"
    PROJECT_MANAGER = "project_manager"
    WORKER = "worker"


class Worker(Base):
    __tablename__ = "workers"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    role = Column(SQLAlchemyEnum(*RoleEnum.__members__), default="worker")
    location = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_available = Column(Boolean, default=True)
    user = relationship("User", backref="worker", uselist=False)
    project_workers = relationship(
        "Project", secondary=worker_project, backref="worker_projects"
    )
    skills = relationship("Skill", secondary=worker_skill, back_populates="workers")
