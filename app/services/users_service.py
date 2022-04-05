from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from app.configs.db_config import get_db
from app.schema.user_schema import AuthUserCreateDTO, NewUser
from app.entity.entities import Users, University

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_password_hash(password):
    return crypt_context.hash(password)


# async def sign_up(new_user: NewUser, db: Session):
#     user = Users(username=new_user.username,
#                  password=get_password_hash(new_user.password))
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return {"message": "Created user successfully!"}


def create(dto: AuthUserCreateDTO, db: Session):
    university = db.query(University).filter(University.id == dto.university_id).first()
    dto.password = get_password_hash(dto.password)
    if not university:
        raise HTTPException(
            detail={'error': f'University not found with provided id({dto.university_id})'},
            status_code=status.HTTP_400_BAD_REQUEST)
    user = Users(**dto.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


SECRET_KEY = "3e8a3f31aab886f8793176988f8298c9265f84b8388c9fef93635b08951f379b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password, hashed_password):
    return crypt_context.verify(plain_password, hashed_password)


def authenticate(username, password):
    try:
        user = get_user(username)
        password_check = verify_password(password, user['password'])
        return password_check
    except User.DoesNotExist:
        return False


class Token(BaseModel):
    access_token: str
    token_type: str



class TokenData(BaseModel):
    username: Optional[str] = None


def get_user(username: str, db: Session):
    try:
        user = db.query(Users).filter(Users.username == username).first()
        return user
    except Users.DoesNotExist:
        return None


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
