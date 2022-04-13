from fastapi import Response, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from application.configs.oauth2 import has_role
from application.entity.entities import Book, Users
from application.schema import book_schema as schema


def create(dto: schema.BookCreateDto, db: Session, session_user: Users):
    has_role(session_user.role, 'ADMIN')
    book = Book(**dto.dict())
    book.created_by = session_user.id
    book.university_id = session_user.university_id
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_all(db: Session):
    return db.query(Book).all()


def get(book_id: int, db: Session):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book not found with id : '{book_id}'")

    return book


def update(dto: schema.BookUpdateDto, db: Session, session_user: Users):

    has_role(session_user.role, 'ADMIN')

    book_query = db.query().filter(Book.id == dto.id)
    book: Book = book_query.first()

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book not found with id : '{id}'")

    if book.university_id != session_user.university_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'error': 'Forbidden'})

    book.update(dto.dict(), synchronize_session=False)
    db.commit()

    return True


def delete(book_id: int, db: Session, session_user: Users):
    has_role(session_user.role, 'ADMIN')
    book_query = db.query(Book).filter(Book.id == book_id)
    book: Book = book_query.first()

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article not found with id : '{book_id}'")

    if book.university_id != session_user.university_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'error': 'Forbidden'})

    book_query.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
