from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import JWTtoken as jt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Could not validate credentials", 
        headers={"WWW-Authenticate": "Bearer"}
    )
    return jt.verify_token(token, credentials_exception)
