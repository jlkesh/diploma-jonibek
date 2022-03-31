from app.schema import book_schema as schema
from app.entity.entities import Book

from sqlalchemy.orm import Session

from fastapi.responses import UJSONResponse
from fastapi.exceptions import HTTPException
from fastapi import Response, status


def create(dto: schema.BookCreateDto, db: Session):
    book = Book(**dto.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_all(db: Session):
    return db.query(Book).all()


def get(id: int, db: Session):
    book = db.query(Book).filter(Book.id == id).first()

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book not found with id : '{id}'")

    return book


def update(dto: schema.BookUpdateDto, db: Session):
    book_query = db.query().filter(Book.id == dto.id)

    book: Book = book_query.first()

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book not found with id : '{id}'")

    book.update(dto.dict(), synchronize_session=False)

    db.commit()

    return True


def delete(id: int, db: Session):
    book_query = db.query(Book).filter(Book.id == id)

    book: Book = book_query.first()

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article not found with id : '{id}'")

    book_query.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
