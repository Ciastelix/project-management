from fastapi import APIRouter, status, Depends
from models.schemas.project import ProjectInCreate, ProjectInResponse, ProjectInUpdate
from dependency_injector.wiring import Provide, inject
from services.project import ProjectService
from container import Container
from uuid import UUID

router = APIRouter()

@router.get("/", response_model=list[ProjectInResponse], status_code=status.HTTP_200_OK)
@inject
def read_projects(project_service: ProjectService = Depends(Provide[Container.project_service])):
    return project_service.get_all()

@router.post("/", response_model=ProjectInResponse, status_code=status.HTTP_201_CREATED)
@inject
def create_project(project: ProjectInCreate, project_service: ProjectService = Depends(Provide[Container.project_service])):
    return project_service.add(project)

@router.get("/{project_id}", response_model=ProjectInResponse, status_code=status.HTTP_200_OK)
@inject
def read_project(project_id: UUID, project_service: ProjectService = Depends(Provide[Container.project_service])):
    return project_service.get_by_id(project_id)

@router.put("/{project_id}", response_model=ProjectInResponse, status_code=status.HTTP_200_OK)
@inject
def update_project(project_id: UUID, project: ProjectInUpdate, project_service: ProjectService = Depends(Provide[Container.project_service])):
    return project_service.update(project_id, project)

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def delete_project(project_id: UUID, project_service: ProjectService = Depends(Provide[Container.project_service])):
    return project_service.delete(project_id)

@router.put("/{project_id}/add_to_project/{worker_id}", response_model=ProjectInResponse, status_code=status.HTTP_200_OK)
@inject
def add_to_project(project_id: UUID, worker_id: UUID, project_service: ProjectService = Depends(Provide[Container.project_service])):
    return project_service.add_to_project(project_id, worker_id)

@router.put("/{project_id}/remove_from_project/{worker_id}", response_model=ProjectInResponse, status_code=status.HTTP_200_OK)
@inject
def remove_from_project(project_id: UUID, worker_id: UUID, project_service: ProjectService = Depends(Provide[Container.project_service])):
    return project_service.remove_from_project(project_id, worker_id)

