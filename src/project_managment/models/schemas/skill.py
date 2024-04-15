from pydantic import BaseModel
from uuid import UUID

class SkillInCreate(BaseModel):
    name: str

class SkillInDB(SkillInCreate):
    id: UUID
    class Config:
        from_attributes = True
        
class SkillInResponse(SkillInDB):
    pass

class SkillInUpdate(BaseModel):
    name: str
    class Config:
        from_attributes = True

