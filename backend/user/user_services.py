from sqlalchemy.orm import Session
from databases.models import User
from typing import Optional
from .user_utils import hash_password
from fastapi import HTTPException


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def get_user_by_email(self, email: str):
        user = self.db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def create_user(
        self, email: str, username: str, password: str, pin: Optional[str] = None
    ):
        hashed = hash_password(password)
        new_user = User(email=email, username=username, hashed_password=hashed, pin=pin)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def update_user(
        self,
        user_id: int,
        username: Optional[str] = None,
        password: Optional[str] = None,
        pin: Optional[str] = None,
    ):
        user = self.get_user_by_id(user_id)
        if username:
            user.username = username
        if password:
            user.hashed_password = hash_password(password)
        if pin is not None:
            user.pin = pin
        self.db.commit()

    def verify_pin(self, user_id: int, pin: str) -> bool:
        user = self.get_user_by_id(user_id)
        if not user.pin:
            return True
        return user.pin == pin

    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        self.db.delete(user)
        self.db.commit()
