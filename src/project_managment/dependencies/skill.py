from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session  
from models.domain.skill import Skill
from models.schemas.skill import SkillInCreate, SkillInUpdate
from uuid import UUID
class SkillRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]] ) -> None:
        self.session_factory = session_factory
        

    def add(self, skill:SkillInCreate) -> Skill:
        with self.session_factory() as session:
            skill = Skill(**skill.model_dump())
            session.add(skill)
            session.commit()
            session.refresh(skill)
        return skill

    def get_all(self) -> list[Skill]:
        with self.session_factory() as session:
            return session.query(Skill).all()

    
    def get_by_id(self, skill_id:UUID) -> Skill:
        with self.session_factory() as session:
            return session.query(Skill).filter_by(id=skill_id).first()

    def update(self, skill_id:UUID, skill_new: SkillInUpdate) -> Skill:
        with self.session_factory() as session:
            skill = session.query(Skill).filter_by(id=skill_id).first()
            if skill is not None:
                for key, value in skill_new.model_dump().items():
                    setattr(skill, key, value)

                session.commit()
                session.refresh(skill)
            return skill

    def delete(self, skill_id:UUID) -> None:
        with self.session_factory() as session:
            skill = session.query(Skill).filter_by(id=skill_id).first()
            session.delete(skill)
            session.commit()

    def add_to_skill(self, skill_id:UUID, worker_id:UUID) -> Skill:
        with self.session_factory() as session:
            skill = session.query(Skill).filter_by(id=skill_id).first()
            skill.workers.append(worker_id)
            session.commit()
            session.refresh(skill)
        return skill


    def remove_from_skill(self, skill_id:UUID, worker_id:UUID) -> Skill:
        with self.session_factory() as session:
            skill = session.query(Skill).filter_by(id=skill_id).first()
            skill.workers.remove(worker_id)
            session.commit()
            session.refresh(skill)
        return skill
        
    