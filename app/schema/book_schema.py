from datetime import datetime
from pydantic import validator
from . import Dto, GenericDto


class BookDto(GenericDto):
    name: str
    author: str
    short_info: str
    page_count: int
    created_at: datetime
    created_by: int


class BookCreateDto(Dto):
    name: str
    author: str
    short_info: str
    page_count: int

    @validator('name')
    def validate(cls, arg: str):
        if not arg:
            raise ValueError('Title Cannot be null')
        if arg.isspace():
            raise ValueError('Title Cannot be blank')
        return arg.title()

    @validator('short_info')
    def validater(cls, valid: str):
        if not valid:
            raise ValueError("Short body Cannot be null")
        if valid.isspace():
            raise ValueError("Short body be blank")
        return valid

    @validator('page_count')
    def validator(cls, valid: int):
        if not valid:
            raise ValueError("Page Cannot be null")
        if valid <= 0:
            raise ValueError("The book should be at least 1 page long")

    class Config:
        orm_mode = True


class BookUpdateDto(GenericDto):
    title: str
    short: str
    description: str
    published: bool = False
