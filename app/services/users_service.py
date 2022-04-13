from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.hash import pbkdf2_sha256, bcrypt
from pydantic import BaseModel
from app.configs.db_config import get_db
from app.schema.user_schema import AuthUserCreateDTO
from app.entity.entities import Users, University
from app.schema import user_schema as schemas

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/token")


def get_password_hash(password):
    return bcrypt.hash(password)


async def create(dto: AuthUserCreateDTO, db: Session):
    university = db.query(University).filter(University.id == dto.university_id).first()
    dto.password = await get_password_hash(dto.password)
    if not university:
        raise HTTPException(
            detail={'error': f'University not found with provided id({dto.university_id})'},
            status_code=status.HTTP_400_BAD_REQUEST)
    user = await Users(**dto.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password, hashed_password):
    return bcrypt.verify(plain_password, hashed_password)


def authenticate(username, password, db):
    try:
        user = get_user(username, db)
        password_check = verify_password(password, user.password)
        return password_check
    except Exception:
        return False


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


def get_user(username: str, db):
    try:
        user = db.query(Users).filter(Users.username == username).first()
        return user
    except Exception:
        return None


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
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
    user = get_user(username=token_data.username, db=db)
    if user is None:
        raise credentials_exception
    return schemas.User.from_orm(user)
