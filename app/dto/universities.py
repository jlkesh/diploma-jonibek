from datetime import datetime
from pydantic import BaseModel, validator, ValidationError
from app.dto import GenericDto


class UniversityDto(GenericDto):
    name: str
    description: str
    created_at: datetime
    owner: int

    class Config:
        orm_mode = True


class UniversityCreateDto(BaseModel):
    name: str
    description: str
    owner: int


class UniversityUpdateDto(GenericDto):
    name: str
    description: str
    owner: int
