from sqlalchemy.orm import Session
from user.user_services import UserService
from user.user_utils import verify_password
from fastapi import HTTPException
from .jwt_service import JwtService, TokenPayLoad

class AuthServices:
    def __init__(self, db: Session):
        self.db = db
        self.user_service = UserService(db)
        self.jwt_service = JwtService()

    def login(self, email: str, password: str):
        user = self.user_service.get_user_by_email(email)
        if not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Incorrect Password")
        payload = TokenPayLoad(email=user.email, id=user.id)
        return {
            "access_token": self.jwt_service.create_access_token(payload),
            "refresh_token": self.jwt_service.create_refresh_token(payload)
        }

    def refresh(self, refresh_token: str):
        if not refresh_token:
            raise HTTPException(status_code=401, detail="Refresh Token not found")
        payload = self.jwt_service.verify_token(refresh_token)
        return {"access_token": self.jwt_service.create_access_token(payload)}
