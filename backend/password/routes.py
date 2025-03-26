from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from auth.auth_guard import auth_guard
from databases.database import get_db
from .password_services import PasswordService
from .dtos import PasswordCreateDto, PasswordUpdateDto
from .password_generation import PasswordGenerator

password_router = APIRouter()


@password_router.post("")
def create_password(
    dto: PasswordCreateDto,
    db: Session = Depends(get_db),
    user_payload=Depends(auth_guard),
):
    service = PasswordService(db)
    return service.create_password(
        user_payload.id, dto.site_name, dto.encrypted_password
    )


@password_router.get("")
def get_passwords(db: Session = Depends(get_db), user_payload=Depends(auth_guard)):
    service = PasswordService(db)
    return service.get_passwords(user_payload.id)


@password_router.get("/{password_id}")
def get_password(
    password_id: int, db: Session = Depends(get_db), user_payload=Depends(auth_guard)
):
    service = PasswordService(db)
    return service.get_password(user_payload.id, password_id)


@password_router.patch("/{password_id}")
def update_password(
    password_id: int,
    dto: PasswordUpdateDto,
    db: Session = Depends(get_db),
    user_payload=Depends(auth_guard),
):
    service = PasswordService(db)
    return service.update_password(
        user_payload.id, password_id, dto.site_name, dto.encrypted_password
    )


@password_router.delete("/{password_id}")
def delete_password(
    password_id: int, db: Session = Depends(get_db), user_payload=Depends(auth_guard)
):
    service = PasswordService(db)
    return service.delete_password(user_payload.id, password_id)


@password_router.get("/generate")
def generate_random_password(noSpecialChars: bool = Query(False)):
    return {"generated_password": PasswordGenerator.generate(noSpecialChars)}
