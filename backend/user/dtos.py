from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Annotated, Optional

class CreateUserDto(BaseModel):
    username: str
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=8, max_length=100)]

class UpdateUserDto(BaseModel):
    username: Optional[str] = None
    password: Optional[Annotated[str, StringConstraints(min_length=8, max_length=100)]] = None
