from datetime import datetime
from pydantic import BaseModel
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

    class Config:
        orm_mode = True


class BookUpdateDto(GenericDto):
    title: str
    short: str
    description: str
    published: bool = False
