from fastapi import APIRouter
from dtos import LoginDto, RefreshDto
auth_router = APIRouter()


@auth_router.post("/login")
def login(dto: LoginDto):
    pass


@auth_router.post("/logout")
def logout():
    pass

@auth_router.post("/refresh")
def  refresh_token(dto: RefreshDto):
    pass