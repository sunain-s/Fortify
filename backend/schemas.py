from pydantic import BaseModel, Field, StringConstraints
from typing import Optional, Annotated
from datetime import datetime

# ---------------------------
# User Schemas
# ---------------------------

class UserCreate(BaseModel):
    username: Annotated[str, StringConstraints(min_length=3, max_length=50)]
    password: Annotated[str, StringConstraints(min_length=3, max_length=100)]

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

# ---------------------------
# JWT Token Schemas
# ---------------------------

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    user_id: Optional[int] = None

# ---------------------------
# Vault Entry Schemas
# ---------------------------

class VaultEntryCreate(BaseModel):
    service: str = Field(..., example="GitHub")
    encrypted_username: str = Field(..., example="encrypted_username_string")
    encrypted_password: str = Field(..., example="encrypted_password_string")
    metadata: Optional[str] = Field(None, example="Personal account details")

class VaultEntryOut(BaseModel):
    id: int
    service: str
    encrypted_username: str
    encrypted_password: str
    metadata: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class VaultEntryUpdate(BaseModel):
    service: Optional[str] = Field(None, example="GitHub")
    encrypted_username: Optional[str] = Field(None, example="updated_encrypted_username")
    encrypted_password: Optional[str] = Field(None, example="updated_encrypted_password")
    metadata: Optional[str] = Field(None, example="Updated account details")
