from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from application.configs.db_config import get_db
from application.configs.settings import settings
from application.entity.entities import Users
from application.schema.user_schema import TokenData

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/users/login")


def generate_access_token(data: dict):
    to_encode = data.copy()
    expiry = datetime.now() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({
        'exp': expiry, })
    encoded_token = jwt.encode(to_encode, settings.secret_key, settings.algorithm)
    return encoded_token


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=settings.algorithm)
        user_id: str = payload.get('user_id')
        if not user_id:
            raise credentials_exception
        return TokenData(id=user_id)
    except JWTError:
        raise credentials_exception


def get_session_user(db: Session = Depends(get_db), token: str = Depends(oauth2_schema)) -> Users:
    from application.services import users_service
    credentials_exception = HTTPException(
        detail={'error': 'Could not validate credentials'},
        headers={'WWW-Authenticate': 'Bearer'},
        status_code=status.HTTP_401_UNAUTHORIZED)

    token_data = verify_access_token(token, credentials_exception)

    session_user: Users = users_service.session_user(db=db, token_data=token_data)

    if not session_user.is_active:
        raise HTTPException(
            detail={'error': 'User is inactive'},
            headers={'WWW-Authenticate': 'Bearer'},
            status_code=status.HTTP_401_UNAUTHORIZED)

    return session_user


def has_role(session_user_role, checking_role):
    if session_user_role != checking_role:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'error': 'Forbidden'})


def has_roles(session_user_role, checking_role: list):
    if session_user_role not in checking_role:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'error': 'Forbidden'})
