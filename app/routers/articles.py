from fastapi import APIRouter, Depends, status

from app.services import article as service
from app.schema import article_schema as schema
from sqlalchemy.orm import Session
from app.configs.db_config import get_db
from app import _http

router = APIRouter(tags=['Article Router'], prefix="/articles")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(dto: schema.ArticleCreateDto, db: Session = Depends(get_db)):
    return service.create(dto, db)


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/{id}", response_model=schema.ArticleDto, responses=_http.get_article)
def get(id: int, db: Session = Depends(get_db)):
    return service.get(id, db)


@router.put("/")
def update(dto: schema.ArticleUpdateDto, db: Session = Depends(get_db)):
    return service.update(dto, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def get(id: int, db: Session = Depends(get_db)):
    return service.delete(id, db)







