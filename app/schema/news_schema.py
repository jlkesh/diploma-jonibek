# from datetime import datetime
from pydantic import BaseModel
from . import Dto, GenericDto

# id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
# title: str = Column(String(300))
# body: str = Column(String)
# created_at: datetime = Column(DateTime, nullable=False, server_default='now')
# created_by: int = Column(Integer, ForeignKey('user.id'), nullable=False)

class NewsDto(GenericDto):
    title: str
    body: str
    created: int
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
