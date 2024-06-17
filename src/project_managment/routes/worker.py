from fastapi import APIRouter, status, Depends
from models.schemas.worker import WorkerInCreate, WorkerInUpdate, WorkerInResponse
from dependency_injector.wiring import Provide, inject
from services.worker import WorkerService
from container import Container
from uuid import UUID
from models.schemas.user import UserInCreate

router = APIRouter()


@router.get("/", response_model=list[WorkerInResponse], status_code=status.HTTP_200_OK)
@inject
def read_workers(
    worker_service: WorkerService = Depends(Provide[Container.worker_service]),
):
    return worker_service.get_all()


@router.post("/", response_model=WorkerInResponse, status_code=status.HTTP_201_CREATED)
@inject
def create_worker(
    worker: WorkerInCreate,
    user: UserInCreate,
    worker_service: WorkerService = Depends(Provide[Container.worker_service]),
):
    return worker_service.add(worker, user)


@router.get(
    "/{worker_id}", response_model=WorkerInResponse, status_code=status.HTTP_200_OK
)
@inject
def read_worker(
    worker_id: UUID,
    worker_service: WorkerService = Depends(Provide[Container.worker_service]),
):
    return worker_service.get_by_id(worker_id)


@router.put(
    "/{worker_id}", response_model=WorkerInCreate, status_code=status.HTTP_200_OK
)
@inject
def update_worker(
    worker_id: UUID,
    worker: WorkerInUpdate,
    worker_service: WorkerService = Depends(Provide[Container.worker_service]),
):
    return worker_service.update(worker_id, worker)


@router.delete("/{worker_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def delete_worker(
    worker_id: UUID,
    worker_service: WorkerService = Depends(Provide[Container.worker_service]),
):
    return worker_service.delete(worker_id)


@router.put(
    "/{worker_id}/add_to_project/{project_id}",
    response_model=WorkerInCreate,
    status_code=status.HTTP_200_OK,
)
@inject
def add_to_project(
    worker_id: UUID,
    project_id: UUID,
    worker_service: WorkerService = Depends(Provide[Container.worker_service]),
):
    return worker_service.add_to_project(worker_id, project_id)


@router.put(
    "/{worker_id}/add_skill/{skill_id}",
    response_model=WorkerInCreate,
    status_code=status.HTTP_200_OK,
)
@inject
def add_skill(
    worker_id: UUID,
    skill_id: UUID,
    worker_service: WorkerService = Depends(Provide[Container.worker_service]),
):
    return worker_service.add_skill(worker_id, skill_id)


@router.put(
    "/{worker_id}/remove_from_project/{project_id}",
    response_model=WorkerInCreate,
    status_code=status.HTTP_200_OK,
)
@inject
def remove_from_project(
    worker_id: UUID,
    project_id: UUID,
    worker_service: WorkerService = Depends(Provide[Container.worker_service]),
):
    return worker_service.remove_from_project(worker_id, project_id)


@router.put(
    "/{worker_id}/remove_skill/{skill_id}",
    response_model=WorkerInCreate,
    status_code=status.HTTP_200_OK,
)
@inject
def remove_skill(
    worker_id: UUID,
    skill_id: UUID,
    worker_service: WorkerService = Depends(Provide[Container.worker_service]),
):
    return worker_service.remove_skill(worker_id, skill_id)


@router.put(
    "/asign_user", response_model=WorkerInCreate, status_code=status.HTTP_200_OK
)
@inject
def asign_user(
    worker_id: str,
    user_id: str,
    worker_service: WorkerService = Depends(Provide[Container.worker_service]),
):
    worker_id = UUID(worker_id)
    user_id = UUID(user_id)
    return worker_service.asign_user(worker_id, user_id)
