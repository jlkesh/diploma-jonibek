from datetime import datetime
from typing import Optional
import uuid

from pydantic import BaseModel, validator,ValidationError
from fastapi.exceptions import RequestValidationError

from app.dto import Dto, GenericDto


class ArticleDto(GenericDto):
    title: str
    short: str
    description: str
    published: bool
    created_at: datetime
    created_by: Optional[int] = None    
    class Config:
        orm_mode = True


class ArticleCreateDto(BaseModel):
    title: str
    short: str
    description: str
    published: bool = False
    class Config:
        schema_extra = {
            "example": {
                "title": "Russia's war has cost Ukraine $564.9bn so far - Ukraine",
                "short": """Russia's war on Ukraine has cost Ukraine $564.9bn (£429.3bn) so far in terms of damage to infrastructure""",
                "description": """Russian officials deny there is censorship in Russia. Only laws that need to be obeyed.In fact, under the country’s constitution, censorship is forbidden.""",
                "published": True
                }
            }


    @validator('title')
    def valid_title(cls, v: str):
        if not v:
            print(uuid.uuid4())
            raise RequestValidationError('Title Cannot be null')
        
        if v.isspace():
            raise RequestValidationError('Title Cannot be blank')
        
        return v.title()

    @validator('short')
    def valid_short_info(cls, v: str):
        if not v:
            raise ValidationError('Short Description Cannot be null')
        
        if v.isspace() :
            raise ValidationError('Short Description cannot be blank')
        
        return v




class ArticleUpdateDto(GenericDto):
    title: str
    short: str
    description: str
    published: bool = False
