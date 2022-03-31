from datetime import datetime
from pydantic import BaseModel, validator, ValidationError
from app.dto import GenericDto
from app import _http

class UniversityDto(GenericDto):
    name: str
    abbr: str
    description: str
    created_at: datetime

    class Config:
        orm_mode = True


class UniversityCreateDto(BaseModel):
    name: str
    abbr: str
    description: str


class UniversityUpdateDto(GenericDto):
    name: str
    abbr: str
    description: str
