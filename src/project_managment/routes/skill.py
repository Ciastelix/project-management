from fastapi import APIRouter, status, Depends
from models.schemas.skill import SkillInCreate, SkillInResponse, SkillInUpdate
from dependency_injector.wiring import Provide, inject
from services.skill import SkillService
from container import Container
from uuid import UUID
        

router = APIRouter()

@router.get("/", response_model=list[SkillInResponse], status_code=status.HTTP_200_OK)
@inject
def read_skills(skill_service: SkillService = Depends(Provide[Container.skill_service])):
    return skill_service.get_all()

@router.post("/", response_model=SkillInResponse, status_code=status.HTTP_201_CREATED)
@inject
def create_skill(skill: SkillInCreate, skill_service: SkillService = Depends(Provide[Container.skill_service])):
    return skill_service.add(skill)

@router.get("/{skill_id}", response_model=SkillInResponse, status_code=status.HTTP_200_OK)
@inject
def read_skill(skill_id: UUID, skill_service: SkillService = Depends(Provide[Container.skill_service])):
    return skill_service.get_by_id(skill_id)

@router.put("/{skill_id}", response_model=SkillInResponse, status_code=status.HTTP_200_OK)
@inject
def update_skill(skill_id: UUID, skill: SkillInUpdate, skill_service: SkillService = Depends(Provide[Container.skill_service])):
    return skill_service.update(skill_id, skill)

@router.delete("/{skill_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def delete_skill(skill_id: UUID, skill_service: SkillService = Depends(Provide[Container.skill_service])):
    return skill_service.delete(skill_id)

@router.put("/{skill_id}/add_to_skill/{worker_id}", response_model=SkillInResponse, status_code=status.HTTP_200_OK)
@inject
def add_to_skill(skill_id: UUID, worker_id: UUID, skill_service: SkillService = Depends(Provide[Container.skill_service])):
    return skill_service.add_to_skill(skill_id, worker_id)

@router.put("/{skill_id}/remove_from_skill/{worker_id}", response_model=SkillInResponse, status_code=status.HTTP_200_OK)
@inject
def remove_from_skill(skill_id: UUID, worker_id: UUID, skill_service: SkillService = Depends(Provide[Container.skill_service])):
    return skill_service.remove_from_skill(skill_id, worker_id)
