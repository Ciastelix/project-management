from uuid import UUID
from models.schemas.project import ProjectInCreate, ProjectInUpdate
from models.domain.project import Project
from dependencies.project import ProjectRepository

class ProjectService:
    def __init__(self, project_repository: ProjectRepository) -> None:
        self.project_repository = project_repository

    def add(self, project:ProjectInCreate) -> Project:
        return self.project_repository.add(project)

    def get_all(self) -> list[Project]:
        return self.project_repository.get_all()

    def get_by_id(self, project_id:UUID) -> Project:
        return self.project_repository.get_by_id(project_id)

    def update(self, project_id:UUID, project_new: ProjectInUpdate) -> Project:
        return self.project_repository.update(project_id, project_new)

    def delete(self, project_id:UUID) -> None:
        return self.project_repository.delete(project_id)

    def add_to_project(self, project_id:UUID, worker_id:UUID) -> Project:
        return self.project_repository.add_to_project(project_id, worker_id)

    def remove_from_project(self, project_id:UUID, worker_id:UUID) -> Project:
        return self.project_repository.remove_from_project(project_id, worker_id)