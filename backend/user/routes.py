from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from user_services import UserService
from databases.database import get_db
from  dtos import CreateUserDto

user_router = APIRouter()

@user_router.post("/register")
def createUser(dto: CreateUserDto, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user_service.create_user(dto.email, dto.username, dto.password)
    return {"message": "User successfully created"}
    
@user_router.patch("/{id}")
def updateUser(id: int,dto: CreateUserDto, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user_service.update_user(id, dto.username, hashed_password=dto.password) 
    return {"message": "User successfully updated"}

@user_router.delete("/{id}")
def deleteUser(id: int,  db: Session = Depends(get_db)):
    user_service = UserService(db)
    user_service.delete_user(id)
    return {"message": "User successfully deleted"}