from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class UserInCreate(BaseModel):
    username: str
    email: str
    password: str


class UserInDB(BaseModel):
    username: str
    email: str


class UserInResponse(BaseModel):
    id: UUID
    username: str
    email: str


class UserInUpdate(BaseModel):
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]
    is_active: Optional[bool]
