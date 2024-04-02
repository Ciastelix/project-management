from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session  
from models.domain.project import Project
from models.schemas.project import ProjectInCreate, ProjectInUpdate
from uuid import UUID
class ProjectRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]] ) -> None:
        self.session_factory = session_factory
        

    def add(self, project:ProjectInCreate) -> Project:
        with self.session_factory() as session:
            project = Project(**project.model_dump())
            session.add(project)
            session.commit()
            session.refresh(project)
        return project

    def get_all(self) -> list[Project]:
        with self.session_factory() as session:
            return session.query(Project).all()

    
    def get_by_id(self, project_id:UUID) -> Project:
        with self.session_factory() as session:
            return session.query(Project).filter_by(id=project_id).first()

    def update(self, project_id:UUID, project_new: ProjectInUpdate) -> Project:
        with self.session_factory() as session:
            project = session.query(Project).filter_by(id=project_id).first()
            if project is not None:
                for key, value in project_new.model_dump().items():
                    setattr(project, key, value)

                session.commit()
                session.refresh(project)
            return project

    def delete(self, project_id:UUID) -> None:
        with self.session_factory() as session:
            project = session.query(Project).filter_by(id=project_id).first()
            session.delete(project)
            session.commit()

    def add_to_project(self, project_id:UUID, worker_id:UUID) -> Project:
        with self.session_factory() as session:
            project = session.query(Project).filter_by(id=project_id).first()
            project.workers.append(worker_id)
            session.commit()
            session.refresh(project)
        return project


    def remove_from_project(self, project_id:UUID, worker_id:UUID) -> Project:
        with self.session_factory() as session:
            project = session.query(Project).filter_by(id=project_id).first()
            project.workers.remove(worker_id)
            session.commit()
            session.refresh(project)
        return project
        
    