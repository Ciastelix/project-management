from typing import Optional
from pydantic import BaseModel
from uuid import UUID
from .project import ProjectInResponse as Project
from .skill import SkillInResponse as Skill


class UserInCreate(BaseModel):
    username: str
    email: str
    password: str
    name: str
    surname: str
    role: Optional[str] = "worker"


class UserInDB(BaseModel):
    username: str
    email: str


class WorkerInDB(BaseModel):
    id: UUID
    projects: list[Project]
    skills: list[Skill]


class WorkerInResponseUser(BaseModel):
    id: UUID
    name: str
    surname: str
    username: str
    email: str
    is_active: bool


class UserInResponse(BaseModel):
    id: UUID
    name: str
    surname: str
    username: str
    email: str
    is_active: bool
    worker: Optional[WorkerInDB] = None


class UserInUpdate(BaseModel):
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]
    is_active: Optional[bool]
