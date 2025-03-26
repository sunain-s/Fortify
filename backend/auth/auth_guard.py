import jwt
from fastapi import Depends, Request, HTTPException, status
from fastapi.security import HTTPBearer
from .jwt_service import SECRET_KEY, ALGORITHM, TokenPayLoad

security = HTTPBearer()


def auth_guard(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not Auntheticated, access token missing",
        )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        id: int = payload.get("id")
        return TokenPayLoad(email, id)
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate Credentials",
        )
