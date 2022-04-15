import uuid
from datetime import datetime

from pydantic import validator

from . import Dto, GenericDto
from ..schema_config import NewsCreateConfig


class NewsDto(GenericDto):
    title: str
    body: str
    created_at: datetime
    created_by: int


class NewsCreateDto(NewsCreateConfig):
    title: str
    body: str

    @validator("title")
    def valid_title(cls, v):
        if not v:
            raise ValueError('Title Cannot be null')
        if v.isspace():
            raise ValueError('Title Cannot be blank')
        if not isinstance(v, str):
            raise TypeError("Title not text field")
        return v.title()

    @validator("body")
    def valid_body(cls, v: str):
        if not v:
            raise ValueError('Description or body Cannot be null')
        if v.isspace():
            raise ValueError('Description cannot be blank')
        if not isinstance(v, str):
            raise TypeError("Body please enter in text format")
        return v


class NewsUpdateDto(GenericDto):
    title: str
    body: str

    @validator("title")
    def valid_title(cls, v):
        if not v:
            raise ValueError('Title Cannot be null')
        if v.isspace():
            raise ValueError('Title Cannot be blank')
        return v.title()

    @validator("body")
    def valid_body(cls, v: str):
        if not v:
            raise ValueError('Description or body Cannot be null')
        if v.isspace():
            raise ValueError('Description cannot be blank')
        return v
