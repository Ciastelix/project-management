from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session  
from services.security import get_password_hash
from models.domain.user import User
from models.domain.worker import Worker
from models.schemas.user import UserInCreate
from models.schemas.worker import WorkerInCreate, WorkerInUpdate
from sqlalchemy.orm import joinedload
from uuid import UUID
class WorkerRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]] ) -> None:
        self.session_factory = session_factory
        

    def add(self, worker:WorkerInCreate, user:UserInCreate) -> User:
        with self.session_factory() as session:
            user.password = get_password_hash(user.password)
            
            user = User(**user.model_dump())
            session.add(user)
            worker = Worker(**worker.model_dump())
            worker.user = user
            session.add(worker)
            session.commit()
            session.refresh(worker)
        return worker

    def get_all(self) -> list[Worker]:
        with self.session_factory() as session:
            return session.query(Worker).options(joinedload(Worker.user),joinedload(Worker.projects), joinedload(Worker.skills)).all()

    
    def get_by_id(self, worker_id:UUID) -> Worker:
        with self.session_factory() as session:
            return session.query(Worker).filter_by(id=worker_id).first()

    def update(self, worker_id:UUID, worker_new: WorkerInUpdate) -> Worker:
        with self.session_factory() as session:
            worker = session.query(Worker).filter_by(id=worker_id).first()
            if worker is not None:
                for key, value in worker_new.model_dump().items():
                    setattr(worker, key, value)

                session.commit()
                session.refresh(worker)
            return worker

    def delete(self, user_id:UUID) -> None:
        with self.session_factory() as session:
            user = session.query(User).filter_by(id=user_id).first()
            session.delete(user)
            session.commit()

    def add_to_project(self, worker_id:UUID, project_id:UUID) -> Worker:
        with self.session_factory() as session:
            worker = session.query(Worker).filter_by(id=worker_id).first()
            worker.projects.append(project_id)
            session.commit()
            session.refresh(worker)
        return worker

    def add_skill(self, worker_id:UUID, skill_id:UUID) -> Worker:
        with self.session_factory() as session:
            worker = session.query(Worker).filter_by(id=worker_id).first()
            worker.skills.append(skill_id)
            session.commit()
            session.refresh(worker)
        return worker

    def remove_from_project(self, worker_id:UUID, project_id:UUID) -> Worker:
        with self.session_factory() as session:
            worker = session.query(Worker).filter_by(id=worker_id).first()
            worker.projects.remove(project_id)
            session.commit()
            session.refresh(worker)
        return worker
    
    def remove_skill(self, worker_id:UUID, skill_id:UUID) -> Worker:
        with self.session_factory() as session:
            worker = session.query(Worker).filter_by(id=worker_id).first()
            worker.skills.remove(skill_id)
            session.commit()
            session.refresh(worker)
        return worker
    
    def get_by_email(self, email:str) -> Worker:
        with self.session_factory() as session:
            return session.query(Worker).filter_by(email=email).first()
        
    