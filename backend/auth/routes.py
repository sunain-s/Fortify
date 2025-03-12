from fastapi import APIRouter, Depends, Response, Request
from sqlalchemy.orm import Session
from dtos import LoginDto, RefreshDto
from databases.database import get_db
from auth_services import AuthServices
auth_router = APIRouter()


@auth_router.post("/login")
def login(dto: LoginDto, response: Response,  db: Session = Depends(get_db)):
    auth_service = AuthServices(db)
    tokens = auth_service.login(dto.email, dto.password)


    response.set_cookie(
        key="refresh_token",
        value=tokens["access_token"],
        httponly=True,
        secure=True,      
        samesite="strict"    
    )

    response.set_cookie(
        key="refresh_token",
        value=tokens["refresh_token"],
        httponly=True,
        secure=True,      
        samesite="strict"    
    )

    return {"message": "Logged in"}


@auth_router.post("/logout")
def logout():
    pass

@auth_router.post("/refresh")
def  refresh_token(dto: RefreshDto, request: Request,  db: Session = Depends(get_db)):
    refresh_token = request.cookies.get("refresh_token")
    auth_service = AuthServices(db)
    token = auth_service.refresh(refresh_token)
    return {"access_token": token["access_token"]}
