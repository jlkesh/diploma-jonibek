from enum import Enum
from typing import Optional
from pydantic import BaseModel


class NewUser(BaseModel):
    username: str
    password: str


class Role(str, Enum):
    EMPLOYEE = 'EMPLOYEE'
    ADMIN = 'ADMIN'


class AuthUserCreateDTO(BaseModel):
    username: str
    password: str
    university_id: int
    is_active: bool = False
    role: Role = Role.EMPLOYEE


class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
