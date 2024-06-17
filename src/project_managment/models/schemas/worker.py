from pydantic import BaseModel
from uuid import UUID
from .project import ProjectInResponse as Project
from .skill import SkillInResponse as Skill
from .user import WorkerInResponseUser as User


class WorkerInCreate(BaseModel):
    location: str


class WorkerInUpdate(BaseModel):

    location: str
    is_active: bool
    is_available: bool


class WorkerInResponse(WorkerInCreate):
    id: UUID
    user: User = None
    projects: list[Project] = []
    skills: list[Skill] = []

    class Config:
        from_attributes = True
