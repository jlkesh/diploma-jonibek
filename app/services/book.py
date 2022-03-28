from sqlalchemy.orm import Session
from app.dto.books import *
from app.entity.entities import Book

def create(dto: BookCreateDto, db: Session):
    pass