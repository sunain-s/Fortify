from pydantic import BaseModel, StringConstraints
from typing import Annotated

class LoginDto(BaseModel):
    email: str
    password: Annotated[str, StringConstraints(min_length=8, max_length=100)]


class RefreshDto(BaseModel):
    refresh_token: str




