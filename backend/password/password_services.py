from sqlalchemy.orm import Session
from databases.models import Password
from fastapi import HTTPException
from .encryption_utils import encrypt_password, decrypt_password


class PasswordService:
    def __init__(self, db: Session):
        self.db = db

    def create_password(self, user_id: int, site_name: str, password: str):
        encrypted_password = encrypt_password(password, user_id)

        record = Password(
            user_id=user_id, site_name=site_name, encrypted_password=encrypted_password
        )
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
        return {
            "id": record.id,
            "site_name": record.site_name,
            "date_created": record.date_created,
            "last_updated": record.last_updated,
        }

    def get_passwords(self, user_id: int):
        passwords = self.db.query(Password).filter(Password.user_id == user_id).all()
        return [
            {
                "id": p.id,
                "site_name": p.site_name,
                "date_created": p.date_created,
                "last_updated": p.last_updated,
            }
            for p in passwords
        ]

    def get_password(self, user_id: int, password_id: int):
        record = (
            self.db.query(Password)
            .filter(Password.id == password_id, Password.user_id == user_id)
            .first()
        )
        if not record:
            raise HTTPException(status_code=404, detail="Password not found")

        decrypted_password = decrypt_password(record.encrypted_password)

        return {
            "id": record.id,
            "site_name": record.site_name,
            "password": decrypted_password,
            "date_created": record.date_created,
            "last_updated": record.last_updated,
        }

    def update_password(
        self,
        user_id: int,
        password_id: int,
        site_name: str | None = None,
        password: str | None = None,
    ):
        record = (
            self.db.query(Password)
            .filter(Password.id == password_id, Password.user_id == user_id)
            .first()
        )
        if not record:
            raise HTTPException(status_code=404, detail="Password not found")

        if site_name:
            record.site_name = site_name

        if password:
            record.encrypted_password = encrypt_password(password)

        self.db.commit()
        self.db.refresh(record)

        return {
            "id": record.id,
            "site_name": record.site_name,
            "date_created": record.date_created,
            "last_updated": record.last_updated,
        }

    def delete_password(self, user_id: int, password_id: int):
        record = (
            self.db.query(Password)
            .filter(Password.id == password_id, Password.user_id == user_id)
            .first()
        )
        if not record:
            raise HTTPException(status_code=404, detail="Password not found")

        self.db.delete(record)
        self.db.commit()
        return {"message": "Password deleted"}
