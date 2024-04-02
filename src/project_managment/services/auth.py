from uuid import UUID
from dependencies.auth import AuthRepository
from models.schemas.user import UserInResponse
class AuthService:
    def __init__(self, auth_repository: AuthRepository) -> None:
        self.auth_repository = auth_repository
        
    def get_current_user(self, token:str) -> UserInResponse:
        return self.auth_repository.get_current_user(token)
    
    def get_user(self, id: str) -> dict:
        return self.auth_repository.get_user(id)
    
    def authenticate_user(self, username: str, password: str):
        return self.auth_repository.authenticate_user(username, password)
    
    def login(self, username:str, password:str) -> dict:
        return self.auth_repository.login(username, password)
    