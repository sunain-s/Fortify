from sqlalchemy.orm import Session
from databases.models import Password
from fastapi import HTTPException

class PasswordService:
    def __init__(self, db: Session):
        self.db = db

    def create_password(self, user_id: int, site_name: str, encrypted_password: str):
        record = Password(user_id=user_id, site_name=site_name, encrypted_password=encrypted_password)
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
        return record

    def get_passwords(self, user_id: int):
        return self.db.query(Password).filter(Password.user_id == user_id).all()

    def get_password(self, user_id: int, password_id: int):
        record = self.db.query(Password).filter(Password.id == password_id, Password.user_id == user_id).first()
        if not record:
            raise HTTPException(status_code=404, detail="Not found")
        return record

    def update_password(self, user_id: int, password_id: int, site_name: str, encrypted_password: str):
        record = self.get_password(user_id, password_id)
        if site_name:
            record.site_name = site_name
        if encrypted_password:
            record.encrypted_password = encrypted_password
        self.db.commit()
        self.db.refresh(record)
        return record

    def delete_password(self, user_id: int, password_id: int):
        record = self.get_password(user_id, password_id)
        self.db.delete(record)
        self.db.commit()
        return {"message": "Deleted"}
