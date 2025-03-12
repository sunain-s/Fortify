from fastapi import APIRouter
import dtos

user_router = APIRouter()

@user_router.post("/register")
def createUser(dto: dtos.CreateUserDto):
    pass