from datetime import datetime

from pydantic import validator

from . import Dto, GenericDto
from ..schema_config import CommentCreateConfig


class CommentDto(GenericDto):
    message: str
    article: int
    created_at: datetime
    created_by: int


class CommentCreateDto(CommentCreateConfig):
    article_id: int
    message: str

    @validator('message')
    def comment_message(cls, arg: str):
        if not arg:
            raise ValueError('Message Cannot be null')
        return arg


class CommentUpdateDto(GenericDto):
    comment_id: int
    message: str

    @validator('message')
    def comment_message(cls, arg: str):
        if not arg:
            raise ValueError('Message Cannot be null')
        return arg
