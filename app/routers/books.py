from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app import _http
from app.schema import book_schema as schema
from app.configs.db_config import get_db
from app.services import book as service

router = APIRouter(tags=['Books Router'], prefix="/books")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(dto: schema.BookCreateDto, db: Session = Depends(get_db)):
    return service.create(dto, db)


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/{id}", response_model=schema.BookDto, responses=_http.get_article)
def get(id: int, db: Session = Depends(get_db)):
    return service.get(id, db)


@router.put("/")
def update(dto: schema.BookUpdateDto, db: Session = Depends(get_db)):
    return service.update(dto, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def get(id: int, db: Session = Depends(get_db)):
    return service.delete(id, db)
