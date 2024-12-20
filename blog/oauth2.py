from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .database import get_db
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from .JWT_token import verify_token
from .schemas import TokenData
from .models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data = verify_token(token)
    user = db.query(User).filter(User.email == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user
