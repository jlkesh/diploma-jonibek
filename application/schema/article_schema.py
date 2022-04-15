from datetime import datetime
from typing import Optional, List
import uuid
from pydantic import validator
from application.schema import GenericDto, Dto
from application.schema.comment_schema import CommentDto
from application.schema.like_schema import LikeDto
from application.schema.universities_schema import UniversityDto
from application.schema_config import ArticleCreateConfig


class ArticleDto(GenericDto):
    title: str
    short: str
    body: str
    published: bool
    created_at: datetime
    created_by: Optional[int] = None
    university: UniversityDto
    like: List[LikeDto]
    comment: List[CommentDto]

    class Config:
        orm_mode = True


class ArticleCreateDto(ArticleCreateConfig):
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

    @validator("body")
    def valid_body(cls, v: str):
        if not v:
            raise ValueError('Body Description Cannot be null')

        if v.isspace():
            raise ValueError('Body Description cannot be blank')
        return v


class ArticleUpdateDto(GenericDto):
    title: str
    short: str
    body: str
    published: bool = False

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

    @validator("body")
    def valid_body(cls, v: str):
        if not v:
            raise ValueError('Body Description Cannot be null')

        if v.isspace():
            raise ValueError('Body Description cannot be blank')
        return v
