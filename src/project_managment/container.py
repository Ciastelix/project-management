from dependency_injector import containers, providers
from db import Database    
from services.user import UserService
from services.worker import WorkerService
from services.project import ProjectService
from services.skill import SkillService
from services.auth import AuthService
from dependencies.user import UserRepository
from dependencies.worker import WorkerRepository
from dependencies.project import ProjectRepository
from dependencies.skill import SkillRepository
from dependencies.auth import AuthRepository

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["routes.user", "routes.worker", "routes.project", "routes.skill"])
    config = providers.Configuration()
    config.db.url.from_env("DB_URL")
    db = providers.Singleton(Database, db_url=config.db.url)
    
    user_repository = providers.Singleton(UserRepository, session_factory=db.provided.session)

    worker_repository = providers.Singleton(WorkerRepository, session_factory=db.provided.session)
    
    project_repository = providers.Singleton(ProjectRepository, session_factory=db.provided.session)
    
    skill_repository = providers.Singleton(SkillRepository, session_factory=db.provided.session)
    
    auth_repository = providers.Singleton(AuthRepository, session_factory=db.provided.session)
    
    user_service = providers.Factory(UserService, user_repository=user_repository)
    
    worker_service = providers.Factory(WorkerService, worker_repository=worker_repository)
    
    project_service = providers.Factory(ProjectService, project_repository=project_repository)
    
    skill_service = providers.Factory(SkillService, skill_repository=skill_repository)
    
    auth_service = providers.Factory(AuthService, auth_repository=auth_repository)
    