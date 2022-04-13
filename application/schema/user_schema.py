from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class NewUser(BaseModel):
    username: str
    password: str


class Role(str, Enum):
    USER = 'USER'
    ADMIN = 'ADMIN'
    SUPER_ADMIN = 'SUPER_ADMIN'


class UserDTO(BaseModel):
    id: int
    username: str
    is_active: bool
    role: str
    university_id: int
    university: int
    created_at: datetime

    class Config:
        orm_mode = True


class UserCreateDTO(BaseModel):
    username: str
    password: str
    university_id: int
    is_active: bool = False
    role: Role = Role.USER


class UserLoginDTO(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
