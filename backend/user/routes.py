from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from .user_services import UserService
from databases.database import get_db
from .dtos import CreateUserDto, UpdateUserDto
from auth.auth_guard import auth_guard

user_router = APIRouter()


@user_router.post("/register")
def createUser(dto: CreateUserDto, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user_service.create_user(dto.email, dto.username, dto.password, dto.pin)
    return {"message": "User created"}


@user_router.patch("")
def updateUser(
    dto: UpdateUserDto, db: Session = Depends(get_db), user_payload=Depends(auth_guard)
):
    user_service = UserService(db)
    user_service.update_user(user_payload.id, dto.username, dto.password, dto.pin)
    return {"message": "User updated"}


@user_router.delete("")
def deleteUser(db: Session = Depends(get_db), user_payload=Depends(auth_guard)):
    user_service = UserService(db)
    user_service.delete_user(user_payload.id)
    return {"message": "User deleted"}


@user_router.get("/me")
def get_me(db: Session = Depends(get_db), user_payload=Depends(auth_guard)):
    user_service = UserService(db)
    user = user_service.get_user_by_id(user_payload.id)
    return {
        "id": user.id,
        "email": user.email,
        "username": user.username,
        "has_pin": bool(user.pin),
    }
