from pydantic import BaseModel, EmailStr, StringConstraints
from  typing import Annotated

class CreateUserDto(BaseModel):
    username: str
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=8, max_length=100)]
    