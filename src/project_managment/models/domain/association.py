from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from project_managment.db import Base

# tabele wiele do wielu
worker_skill = Table('worker_skill', Base.metadata,
    Column('worker_id', UUID(as_uuid=True), ForeignKey('workers.id')),
    Column('skill_id', UUID(as_uuid=True), ForeignKey('skills.id'))
)

worker_project = Table('worker_project', Base.metadata,
    Column('worker_id', UUID(as_uuid=True), ForeignKey('workers.id')),
    Column('project_id', UUID(as_uuid=True), ForeignKey('projects.id'))
)