from datetime import datetime

from pydantic import validator

from . import Dto, GenericDto


class LikeDto(GenericDto):
    is_like: bool
    article_id: int
    created_at: datetime
    created_by: int


class LikeCreateDto(Dto):
    is_like: bool
    article_id: int

    @validator('is_like')
    def valid_is_like(cls, arg: bool):
        if not arg:
            raise ValueError('Like Cannot be null')
        return arg


class LikeUpdateDto(GenericDto):
    is_like: bool

    @validator('is_like')
    def valid_is_like(cls, arg: bool):
        if not arg:
            raise ValueError('Like Cannot be null')
        return arg
