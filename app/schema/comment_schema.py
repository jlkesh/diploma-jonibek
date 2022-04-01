from datetime import datetime
from pydantic import validator
from . import Dto, GenericDto


class CommentDto(GenericDto):
    message: str
    article: int
    created_at: datetime
    created_by: int


class CommentCreateDto(Dto):
    message: str
    article: str

    @validator('message')
    def validate(cls, arg: str):
        if not arg:
            raise ValueError('Message Cannot be null')
        if arg.isspace():
            raise ValueError('Message Cannot be blank')
        return arg.title()

    class Config:
        orm_mode = True


class CommentUpdateDto(GenericDto):
    message: str
