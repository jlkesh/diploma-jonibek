from datetime import datetime
from pydantic import BaseModel, validator
from application.schema import GenericDto, Dto


class UniversityDto(GenericDto):
    name: str
    abbr: str
    description: str
    created_at: datetime

    class Config:
        orm_mode = True


class UniversityCreateDto(Dto):
    name: str
    abbr: str
    description: str

    @validator('name')
    def validate(cls, value: str):
        if not value:
            raise ValueError('University Name Cannot be not null')

    @validator('abbr')
    def valid(cls, value: str):
        if not value:
            raise ValueError()

    @validator('description')
    def validators(cls, description: str):
        if not description:
            raise ValueError("University info Cannot be not null...")
        if description.isspace():
            raise ValueError("University info Cannot be not blank...")


class UniversityUpdateDto(GenericDto):
    name: str
    abbr: str
    description: str
