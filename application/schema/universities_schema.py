from datetime import datetime
from pydantic import BaseModel, validator
from application.schema import GenericDto, Dto
from application.schema_config import UniversityCreateConfig


class UniversityDto(GenericDto):
    name: str
    abbr: str
    description: str
    created_at: datetime

    class Config:
        orm_mode = True


class UniversityCreateDto(UniversityCreateConfig):
    name: str
    abbr: str
    description: str

    @validator('name')
    def valid_name(cls, value: str):
        if not value:
            raise ValueError('University Name Cannot be not null')

    @validator('abbr')
    def valid_abbr(cls, value: str):
        if not value:
            raise ValueError("University Abbr Cannot  be not null")

    @validator('description')
    def valid_description(cls, description: str):
        if not description:
            raise ValueError("University info Cannot be not null...")
        if description.isspace():
            raise ValueError("University info Cannot be not blank...")


class UniversityUpdateDto(GenericDto):
    name: str
    abbr: str
    description: str

    @validator('name')
    def valid_name(cls, value: str):
        if not value:
            raise ValueError('University Name Cannot be not null')

    @validator('abbr')
    def valid_abbr(cls, value: str):
        if not value:
            raise ValueError("University Abbr Cannot  be not null")

    @validator('description')
    def valid_description(cls, description: str):
        if not description:
            raise ValueError("University info Cannot be not null...")
        if description.isspace():
            raise ValueError("University info Cannot be not blank...")
