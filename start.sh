#!/bin/bash
cleanup() {
  echo "Stopping backend and frontend..."
  kill $BACKEND_PID
  kill $FRONTEND_PID
  exit 0
}

trap cleanup SIGINT SIGTERM

source .venv/bin/activate

cd ./src/project_managment

export DB_URL="sqlite:///./db.sqlite3"
export JWT_SECRET="fJJZNs9LnU356LmyTQA8"
export JWT_ALGORITHM="HS256"


uvicorn main:app --reload &> backend.log &
BACKEND_PID=$!


cd ../../front


export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"


nvm use --lts
npm i
npm start &> frontend.log &
FRONTEND_PID=$!


wait $FRONTEND_PID

cleanup