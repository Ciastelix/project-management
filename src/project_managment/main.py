from fastapi import FastAPI
from container import Container
from routes import skill, worker, project, user
container = Container()
db = container.db()
db.create_database()
app = FastAPI()
app.container = container
app.include_router(skill.router, prefix="/skills", tags=["skills"])
app.include_router(worker.router, prefix="/workers", tags=["workers"])
app.include_router(project.router, prefix="/projects", tags=["projects"])
app.include_router(user.router, prefix="/users", tags=["users"])
# add cors
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
