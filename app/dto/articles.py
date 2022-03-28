from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from . import Dto, GenericDto


class ArticleDto(GenericDto):
    title: str
    short: str
    description: str
    published: bool
    created_at: datetime
    created_by: Optional[int] = None

    class Config:
        orm_mode = True


class ArticleCreateDto(Dto):
    title: str
    short: str
    description: str
    published: bool = False


class ArticleUpdateDto(GenericDto):
    title: str
    short: str
    description: str
    published: bool = False
