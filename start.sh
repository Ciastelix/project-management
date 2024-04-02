#!/bin/bash
cd ./src/project_managment
export DB_URL="sqlite:///./db.sqlite3"
export JWT_SECRET="fJJZNs9LnU356LmyTQA8"
export JWT_ALGORITHM="HS256"
uvicorn main:app --reload