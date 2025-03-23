import jwt
from datetime import datetime, timedelta, UTC
from typing import Optional
from pydantic import BaseModel
from fastapi import HTTPException

SECRET_KEY = "secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_MINUTES = 1440

class TokenPayLoad(BaseModel):
    email: str
    id: int

class JwtService:
    def __init__(self):
        pass

    def create_access_token(self, data: TokenPayLoad) -> str:
        to_encode = data.model_dump()
        expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode["exp"] = expire
        to_encode["type"] = "access"
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def create_refresh_token(self, data: TokenPayLoad) -> str:
        to_encode = data.model_dump()
        expire = datetime.now(UTC) + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
        to_encode["exp"] = expire
        to_encode["type"] = "refresh"
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            if payload.get("type") != "refresh":
                raise HTTPException(status_code=401, detail="Invalid token type")
            email = payload.get("email")
            id = payload.get("id")
            if email is None or id is None:
                raise HTTPException(status_code=401, detail="Invalid token payload")
            return TokenPayLoad(email=email, id=id)
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Refresh token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
