import jwt 
from datetime import datetime, timedelta, UTC
from typing import Optional


SECRET_KEY = "secret" #Move this to a .env folder 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15  
REFRESH_TOKEN_EXPIRE_MINUTES = 1440

class jwt_service:
    def __init__(self):
        pass

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        expire = datetime.now(UTC) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire, "type": "access"})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    def create_refresh_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES))
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

