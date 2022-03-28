from datetime import datetime
from pydantic import BaseModel
from . import Dto, GenericDto




class ArticleDto(GenericDto):
    title: str
    short: str
    description: str
    published: bool
    created_at: datetime
    created_by: int


class ArticleCreateDto(Dto):
    title: str
    short: str
    description: str
    published: bool = False


class ArticleUpdateDto(Dto):
    title: str
    short: str
    description: str
    published: bool = False
