from pydantic import BaseModel
from uuid import UUID

class SkillIn(BaseModel):
    name: str

class SkillInDB(SkillIn):
    id: UUID
    class Config:
        orm_mode = True
        
class SkillInResponse(SkillInDB):
    pass

class SkillInUpdate(BaseModel):
    name: str
    class Config:
        orm_mode = True

