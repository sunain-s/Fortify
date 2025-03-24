import jwt 
from datetime import datetime, timedelta, UTC
from typing import Optional
from pydantic import BaseModel
from fastapi import HTTPException


SECRET_KEY = "secret" #Move this to a .env folder 
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
        to_encode = data.model_copy()
        expire = datetime.now(UTC) + (timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire, "type": "access"})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    def create_refresh_token(self, data: TokenPayLoad) -> str:
        to_encode = data.model_copy()
        expire = datetime.now(UTC) + (timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire, "type": "refresh"})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    def decode_token(token: str) -> dict:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise Exception("Token Expired")
        except jwt.PyJWTError as e:
            raise Exception(f"Token Invalid: {str(e)}")
        
    def verify_token(token: str):

        try:
            # Decode the token. This will automatically check the expiration if "exp" is set.
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            
            # Optional: Check the token type (if you include such a claim when generating the token)
            if payload.get("type") != "refresh":
                raise HTTPException(
                    status_code=401,
                    detail="Invalid token type"
                )
            
            # Extract the user identifier (commonly stored in the "sub" claim)
            email = payload.get("email")
            id = payload.get("id")

            if email == None or id == None:
                raise HTTPException(
                    status_code=401,
                    detail="Invalid token payloa d"
                )
            
            return TokenPayLoad(email, id)

        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=401,
                detail="Refresh token expired"
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=401,
                detail="Invalid refresh token"
            )

