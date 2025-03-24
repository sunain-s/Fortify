from pydantic import BaseModel

class PasswordCreateDto(BaseModel):
    site_name: str
    encrypted_password: str

class PasswordUpdateDto(BaseModel):
    site_name: str | None = None
    encrypted_password: str | None = None
