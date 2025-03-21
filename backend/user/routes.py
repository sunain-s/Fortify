from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .user_services import UserService
from databases.database import get_db
from .dtos import CreateUserDto
from auth.auth_guard import auth_guard
user_router = APIRouter()

@user_router.post("/register")
def createUser(dto: CreateUserDto, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user_service.create_user(dto.email, dto.username, dto.password)
    return {"message": "User successfully created"}
    
@user_router.patch("/{id}")
def updateUser(dto: CreateUserDto, db: Session = Depends(get_db), user_payload=Depends(auth_guard)):
    user_service = UserService(db)
    user_service.update_user(user_payload.id, dto.username, hashed_password=dto.password) 
    return {"message": "User successfully updated"}

@user_router.delete("/{id}")
def deleteUser(  db: Session = Depends(get_db),  user_payload=Depends(auth_guard)):
    user_service = UserService(db)
    user_service.delete_user(user_payload.id)
    return {"message": "User successfully deleted"}