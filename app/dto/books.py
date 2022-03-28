from datetime import datetime
from pydantic import BaseModel
from . import Dto, GenericDto




class BookDto(GenericDto):
    title: str
    short: str
    description: str
    published: bool
    created_at: datetime
    created_by: int


class BookCreateDto(Dto):
    title: str
    short: str
    description: str
    published: bool = False


class BookUpdateDto(Dto):
    title: str
    short: str
    description: str
    published: bool = False
