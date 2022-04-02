from datetime import datetime
from pydantic import validator
from . import Dto, GenericDto


class LikeDto(GenericDto):
    is_like: bool
    created_at: datetime
    article_id: int


class LikeCreateDto(Dto):
    is_like: bool
    article_id: int

    @validator('is_like')
    def valid_is_like(cls, arg: bool):
        if not arg:
            raise ValueError('Like Cannot be null')
        return arg

    class Config:
        schema_extra = {
            "example": {
                "is_like": True,
                "article_id": 1
            }
        }

        orm_mode = True


class LikeUpdateDto(GenericDto):
    is_like: bool
