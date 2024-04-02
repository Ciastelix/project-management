from fastapi.security import OAuth2PasswordBearer
from fastapi import  Depends, HTTPException
from datetime import datetime, timedelta
from typing import Optional
import jwt
from os import environ
from jwt import PyJWTError
from fastapi import HTTPException
from datetime import timedelta
from models.domain.user import User
from models.schemas.user import UserInResponse
from services.security import verify_password
from sqlalchemy.orm import Session
from contextlib import AbstractContextManager
from typing import Callable
from fastapi import status
from uuid import UUID
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

SECRET_KEY = environ.get("JWT_SECRET") or "KUGhGukGHkuGKYfgiyt75igtyrt"
ALGORITHM = environ.get("JWT_ALGORITHM") or "HS256"
class AuthRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]] ) -> None:
        self.session_factory = session_factory

    async def get_current_user(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            id_str: str = payload.get("sub")
            if id_str is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token is missing user ID",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        except PyJWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not decode token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        with self.session_factory() as session:
            user = session.query(User).filter_by(id=UUID(id_str)).first()
            if user is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found",
                )
        return UserInResponse(**user.__dict__)

    def get_user(self, id: str):
        with self.session_factory() as session:
            id = UUID(id)
            user = session.query(User).filter_by(id=id).first()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return user

    def authenticate_user(self, username: str, password: str):
        user = self.login(username, password)
        return user

    def login(self, username:str, password:str) -> dict:
        with self.session_factory() as session:
            usr = session.query(User).filter_by(username=username).first()
            if not usr:
                raise HTTPException(
                    status_code=401,
                    detail="Incorrect username or password",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            if verify_password(password, usr.password):
                access_token_expires = timedelta(minutes=30)
                access_token = self.create_access_token(
                    data={"sub": str(usr.id)}, expires_delta=access_token_expires
                )
                return {"access_token": access_token, "token_type": "bearer"}
            
    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
