import uuid
from datetime import datetime

from pydantic import validator

from . import Dto, GenericDto


class NewsDto(GenericDto):
    title: str
    body: str
    created_at: datetime
    created_by: int


class NewsCreateDto(Dto):
    title: str
    body: str

    @validator("title")
    def validate(cls, v):
        if not v:
            raise ValueError('Title Cannot be null')
        if v.isspace():
            raise ValueError('Title Cannot be blank')
        if not isinstance(v, str):
            raise TypeError("Title not text field")
        return v.title()

    @validator("body")
    def valid(cls, v: str):
        if not v:
            raise ValueError('Description or body Cannot be null')
        if v.isspace():
            raise ValueError('Description cannot be blank')
        if not isinstance(v, str):
            raise TypeError("Body please enter in text format")
        return v

    class Config:

        allow_reuse = False
        schema_extra = {
            'example': {
                'title': "DeSantis broaches repeal of Disney World's special self-governing status in Florida",
                'body': 'Florida’s Republican Gov. Ron DeSantis addressed on Thursday the suggestion of repealing a 55-year-old state law that allows Disney to effectively govern itself on the grounds of Walt Disney World, following the company’s public opposition to a controversial parental rights law in Florida.'
            }
        }
        orm_mode = True


class NewsUpdateDto(GenericDto):
    title: str
    body: str
