from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime
class ProjectInCreate(BaseModel):
    name: str
    description: str
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    
class ProjectInDB(ProjectInCreate):
    id: UUID
    class Config:
        from_attributes = True
class ProjectInResponse(ProjectInDB):
    is_active: bool
    
class ProjectInUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    is_active: Optional[bool]
    workers: Optional[list[UUID]]