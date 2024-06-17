from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session
from models.domain.worker import Worker
from models.domain.user import User
from models.schemas.worker import WorkerInCreate, WorkerInUpdate
from sqlalchemy.orm import joinedload
from models.domain.project import Project
from models.domain.skill import Skill
from uuid import UUID
from services.security import get_password_hash
from models.schemas.user import UserInCreate


class WorkerRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    def add(self, worker: WorkerInCreate, user: UserInCreate) -> Worker:
        user.password = get_password_hash(user.password)
        with self.session_factory() as session:
            worker = Worker(**worker.model_dump())
            session.add(worker)
            session.commit()
            user = User(**user.model_dump())
            user.worker = worker
            session.add(user)
            session.commit()
            # Ensure projects and skills are loaded before the session is closed
            worker = (
                session.query(Worker)
                .options(joinedload(Worker.projects), joinedload(Worker.skills))
                .filter(
                    Worker.id == worker.id
                )  # Ensure you're querying the specific worker
                .one()
            )
            # No need to refresh since we're loading it with the required data
        return worker

    def get_all(self) -> list[Worker]:
        with self.session_factory() as session:
            return (
                session.query(Worker)
                .options(
                    joinedload(Worker.user).joinedload(User.worker),
                    joinedload(Worker.projects),
                    joinedload(Worker.skills),
                )
                .all()
            )

    def get_by_id(self, worker_id: UUID) -> Worker:
        with self.session_factory() as session:
            return (
                session.query(Worker)
                .options(
                    joinedload(Worker.user),
                    joinedload(Worker.projects),
                    joinedload(Worker.skills),
                )
                .filter_by(id=worker_id)
                .first()
            )

    def update(self, worker_id: UUID, worker_new: WorkerInUpdate) -> Worker:
        with self.session_factory() as session:
            worker = session.query(Worker).filter_by(id=worker_id).first()
            if worker is not None:
                for key, value in worker_new.model_dump().items():
                    setattr(worker, key, value)

                session.commit()
                session.refresh(worker)
            return worker

    def delete(self, user_id: UUID) -> None:
        with self.session_factory() as session:
            user = session.query(User).filter_by(id=user_id).first()
            session.delete(user)
            session.commit()

    def add_to_project(self, worker_id: UUID, project_id: UUID) -> Worker:
        with self.session_factory() as session:
            worker = session.query(Worker).filter_by(id=worker_id).first()
            project = session.query(Project).filter_by(id=project_id).first()
            if not project:
                raise Exception("Project not found")
            worker.projects.append(project)
            session.commit()
            session.refresh(worker)
        return worker

    def add_skill(self, worker_id: UUID, skill_id: UUID) -> Worker:
        with self.session_factory() as session:
            worker = session.query(Worker).filter_by(id=worker_id).first()
            skill = session.query(Skill).filter_by(id=skill_id).first()
            if not skill:
                raise Exception("Skill not found")
            worker.skills.append(skill)
            session.commit()
            session.refresh(worker)
        return worker

    def remove_from_project(self, worker_id: UUID, project_id: UUID) -> Worker:
        with self.session_factory() as session:
            worker = session.query(Worker).filter_by(id=worker_id).first()
            project = session.query(Project).filter_by(id=project_id).first()
            if not project:
                raise Exception("Project not found")
            worker.projects.remove(project)
            session.commit()
            session.refresh(worker)
        return worker

    def remove_skill(self, worker_id: UUID, skill_id: UUID) -> Worker:
        with self.session_factory() as session:
            worker = session.query(Worker).filter_by(id=worker_id).first()
            skill = session.query(Skill).filter_by(id=skill_id).first()
            if not skill:
                raise Exception("Skill not found")
            worker.skills.remove(skill)
            session.commit()
            session.refresh(worker)
        return worker

    def asign_user(self, worker_id: UUID, user_id: UUID) -> Worker:
        with self.session_factory() as session:
            worker = session.query(Worker).filter_by(id=worker_id).first()
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                raise Exception("User not found")
            worker.user = user
            session.commit()
            session.refresh(worker)
        return worker

    def get_by_email(self, email: str) -> Worker:
        with self.session_factory() as session:
            return session.query(Worker).filter_by(email=email).first()
