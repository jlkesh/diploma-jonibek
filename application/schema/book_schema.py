from datetime import datetime
from pydantic import validator
from . import Dto, GenericDto
from ..schema_config import BookCreateConfig


class BookDto(GenericDto):
    name: str
    author: str
    short_info: str
    page_count: int
    created_at: datetime
    created_by: int


class BookCreateDto(BookCreateConfig):
    name: str
    author: str
    short_info: str
    page_count: int
    file_id: int

    @validator('name')
    def book_name(cls, arg: str):
        if not arg:
            raise ValueError('Title Cannot be null')
        if arg.isspace():
            raise ValueError('Title Cannot be blank')
        return arg.title()

    @validator('short_info')
    def book_short_info(cls, valid: str):
        if not valid:
            raise ValueError("Short body Cannot be null")
        if valid.isspace():
            raise ValueError("Short body be blank")
        return valid

    @validator('page_count')
    def book_page_count(cls, valid: int):
        if not valid:
            raise ValueError("Page Cannot be null")
        if valid <= 0:
            raise ValueError("The book should be at least 1 page long")


class BookUpdateDto(GenericDto):
    name: str
    short_info: str
    page_count: str
    published: bool = False

    @validator('name')
    def book_name(cls, arg: str):
        if not arg:
            raise ValueError('Title Cannot be null')
        if arg.isspace():
            raise ValueError('Title Cannot be blank')
        return arg.title()

    @validator('short_info')
    def book_short_info(cls, valid: str):
        if not valid:
            raise ValueError("Short body Cannot be null")
        if valid.isspace():
            raise ValueError("Short body be blank")
        return valid

    @validator('page_count')
    def book_page_count(cls, valid: int):
        if not valid:
            raise ValueError("Page Cannot be null")
        if valid <= 0:
            raise ValueError("The book should be at least 1 page long")

    orm_mode = True
