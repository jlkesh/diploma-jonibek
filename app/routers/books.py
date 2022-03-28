from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.configs.db_config import get_db
from app.services import book as service
from app.dto.books import (BookCreateDto)

router = APIRouter(tags=['Books Router'], prefix="/books")


@router.post("/")
def create(dto: BookCreateDto, db: Session = Depends(get_db)):
    return service.create(dto, db)


@router.get("/")
def get_all():
    pass


@router.get("/{id}")
def get(id: int):
    pass



@router.put("/{id}")
def get(id: int):
    pass


@router.delete("/{id}")
def get(id: int):
    pass







