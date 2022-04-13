from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from application import http_response
from application.configs.db_config import get_db
from application.configs.oauth2 import get_session_user
from application.entity.entities import Users
from application.schema import book_schema as schema
from application.services import book_service as service

router = APIRouter(tags=['Books Router'], prefix="/books")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(dto: schema.BookCreateDto,
           db: Session = Depends(get_db),
           session_user: Users = Depends(get_session_user)):
    return service.create(dto, db, session_user)


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    # TODO add criteria
    return service.get_all(db)


@router.get("/{id}", response_model=schema.BookDto, responses=http_response.get_article)
def get(book_id: int, db: Session = Depends(get_db)):
    return service.get(book_id, db)


@router.put("/")
def update(dto: schema.BookUpdateDto,
           db: Session = Depends(get_db),
           session_user: Users = Depends(get_session_user)):
    return service.update(dto, db, session_user)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def get(book_id: int,
        db: Session = Depends(get_db),
        session_user: Users = Depends(get_session_user)):
    return service.delete(book_id, db, session_user)
