from models.schemas.worker import WorkerInCreate, WorkerInUpdate
from models.domain.worker import Worker
from models.schemas.user import UserInCreate
from models.domain.user import User
from dependencies.worker import WorkerRepository
from uuid import UUID
     
class WorkerService:
    def __init__(self, worker_repository: WorkerRepository) -> None:
        self.worker_repository = worker_repository

    def add(self, worker:WorkerInCreate,user:UserInCreate) -> User:
        return self.worker_repository.add(worker,user)

    def get_all(self) -> list[Worker]:
        return self.worker_repository.get_all()

    def get_by_id(self, worker_id:UUID) -> Worker:
        return self.worker_repository.get_by_id(worker_id)

    def update(self, worker_id:UUID, worker_new: WorkerInUpdate) -> Worker:
        return self.worker_repository.update(worker_id, worker_new)

    def delete(self, user_id:UUID) -> None:
        return self.worker_repository.delete(user_id)

    def add_to_project(self, worker_id:UUID, project_id:UUID) -> Worker:
        return self.worker_repository.add_to_project(worker_id, project_id)

    def add_skill(self, worker_id:UUID, skill_id:UUID) -> Worker:
        return self.worker_repository.add_skill(worker_id, skill_id)

    def remove_from_project(self, worker_id:UUID, project_id:UUID) -> Worker:
        return self.worker_repository.remove_from_project(worker_id, project_id)
    
    def remove_skill(self, worker_id:UUID, skill_id:UUID) -> Worker:
        return self.worker_repository.remove_skill(worker_id, skill_id)
    
    def get_by_email(self, email:str) -> Worker:
        return self.worker_repository.get_by_email(email)