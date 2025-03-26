from pydantic import BaseModel, StringConstraints
from typing import Annotated


class LoginDto(BaseModel):
    email: str
    password: Annotated[str, StringConstraints(min_length=8, max_length=100)]
    pin: str | None = None


class RefreshDto(BaseModel):
    refresh_token: str
