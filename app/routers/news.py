from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app import _http
from app.configs.db_config import get_db
from app.schema import news_schema as schema
from app.services import news as service

router = APIRouter(tags=['News Router'], prefix="/news")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(dto: schema.NewsCreateDto, db: Session = Depends(get_db)):
    return service.create(dto, db)


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/{id}", response_model=schema.NewsDto, responses=_http.get_article)
def get(id: int, db: Session = Depends(get_db)):
    return service.get(id, db)


@router.put("/")
def update(dto: schema.NewsUpdateDto, db: Session = Depends(get_db)):
    return service.update(dto, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def get(id: int, db: Session = Depends(get_db)):
    return service.delete(id, db)
