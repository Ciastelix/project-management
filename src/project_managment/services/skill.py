from models.domain.skill import Skill
from models.schemas.skill import SkillInCreate, SkillInUpdate
from dependencies.skill import SkillRepository
from uuid import UUID
        
class SkillService:
    def __init__(self, skill_repository: SkillRepository) -> None:
        self.skill_repository = skill_repository

    def add(self, skill:SkillInCreate) -> Skill:
        return self.skill_repository.add(skill)

    def get_all(self) -> list[Skill]:
        return self.skill_repository.get_all()

    def get_by_id(self, skill_id:UUID) -> Skill:
        return self.skill_repository.get_by_id(skill_id)

    def update(self, skill_id:UUID, skill_new: SkillInUpdate) -> Skill:
        return self.skill_repository.update(skill_id, skill_new)

    def delete(self, skill_id:UUID) -> None:
        return self.skill_repository.delete(skill_id)

    def add_to_skill(self, skill_id:UUID, worker_id:UUID) -> Skill:
        return self.skill_repository.add_to_skill(skill_id, worker_id)

    def remove_from_skill(self, skill_id:UUID, worker_id:UUID) -> Skill:
        return self.skill_repository.remove_from_skill(skill_id, worker_id)