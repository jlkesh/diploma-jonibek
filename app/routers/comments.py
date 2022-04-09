from sqlalchemy.orm import Session

from app.configs.db_config import get_db
from app.schema.comment_schema import CommentCreateDto, CommentUpdateDto
from app.services import comments as service
from fastapi import APIRouter, Depends

router = APIRouter(tags=['Comments Router'], prefix="/comments")


@router.post("/{article_id}")
def create_comment(article_id, dto: CommentCreateDto, db: Session = Depends(get_db)):
    return service.create(article_id, dto, db)


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/{id}")
def get(id: int, db: Session = Depends(get_db)):
    return service.get(id, db)


@router.get('/{article_id}')
def get_article_comment(article_id: int, db: Session = Depends(get_db)):
    return service.get_article_comment(article_id, db)


@router.put("/{id}")
def update(id: int, dto: CommentUpdateDto, db: Session = Depends(get_db)):
    return service.update(id, dto, db)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return service.delete(id, db)
