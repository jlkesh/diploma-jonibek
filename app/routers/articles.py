from fastapi import APIRouter, Depends, status

from app.services import article as service
from app.schema import article_schema as schema
from app.schema import user_schema as u_schema
from sqlalchemy.orm import Session
from app.configs.db_config import get_db
from app import _http
from app.services.users_service import get_current_user

router = APIRouter(tags=['Article Router'], prefix="/articles")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(dto: schema.ArticleCreateDto, user: u_schema.User = Depends(get_current_user),
           db: Session = Depends(get_db)):
    return service.create(dto, user, db)


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
