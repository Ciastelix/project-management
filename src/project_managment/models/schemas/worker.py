from pydantic import BaseModel
from uuid import UUID
from .project import ProjectInResponse as Project
from .skill import SkillInResponse as Skill
from .user import UserInResponse as User

class WorkerInCreate(BaseModel):
    role: str
    location: str
    is_active: bool
    is_available: bool
class WorkerInResponse(WorkerInCreate):
    id: UUID
    user: User
    projects: list[Project] = []
    skills: list[Skill] = []
    class Config:
        orm_mode = True
class WorkerInUpdate(BaseModel):
    role: str
    location: str
    is_active: bool
    is_available: bool