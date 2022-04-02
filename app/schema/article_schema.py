from datetime import datetime
from typing import Optional
import uuid

from pydantic import validator

from app.schema import GenericDto, Dto


class ArticleDto(GenericDto):
    title: str
    short: str
    body: str
    published: bool
    created_at: datetime
    created_by: Optional[int] = None

    class Config:
        orm_mode = True


class ArticleCreateDto(Dto):
    title: str
    short: str
    body: str
    published: bool

    @validator("title")
    def valid_title(cls, v: str):
        if not v:
            print(uuid.uuid4())
            raise ValueError('Title Cannot be null')
        if v.isspace():
            raise ValueError('Title Cannot be blank')
        return v.title()

    @validator("short")
    def valid_short(cls, v: str):
        if not v:
            raise ValueError('Short Description Cannot be null')

        if v.isspace():
            raise ValueError('Short Description cannot be blank')
        return v

    class Config:
        schema_extra = {
            "example": {
                "title": "Russia's war has cost Ukraine $564.9bn so far - Ukraine",
                "short": """Russia's war on Ukraine has cost Ukraine $564.9bn (£429.3bn) so far in terms of damage to infrastructure""",
                "body": """Russian officials deny there is censorship in Russia. Only laws that need to be obeyed.In fact, under the country’s constitution, censorship is forbidden.""",
                "published": True
            }
        }


class ArticleUpdateDto(GenericDto):
    title: str
    short: str
    body: str
    published: bool = False
