from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from application import http_response
from application.configs.db_config import get_db
from application.configs.oauth2 import get_session_user
from application.entity.entities import Users
from application.schema import article_schema as schema
from application.services import article_service as service

router = APIRouter(tags=['Article Router'], prefix="/articles")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(dto: schema.ArticleCreateDto,
           db: Session = Depends(get_db),
           session_user: Users = Depends(get_session_user)):
    return service.create(dto, db, session_user)


@router.get("/", response_model=List[schema.ArticleDto])
def get_all(db: Session = Depends(get_db)):
    # TODO add criteria
    return service.get_all(db)


@router.get("/{id}", response_model=schema.ArticleDto, responses=http_response.get_article)
def get(article_id: int, db: Session = Depends(get_db)):
    return service.get(article_id, db)


@router.put("/")
def update(dto: schema.ArticleUpdateDto, db: Session = Depends(get_db), session_user=Depends(get_session_user)):
    return service.update(dto, db, session_user)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def get(article_id: int,
        db: Session = Depends(get_db),
        session_user: Users = Depends(get_session_user)):
    return service.delete(article_id, db, session_user)
