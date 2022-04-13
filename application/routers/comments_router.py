from sqlalchemy.orm import Session

from application.configs.db_config import get_db
from application.configs.oauth2 import get_session_user
from application.entity.entities import Users
from application.schema.comment_schema import CommentCreateDto, CommentUpdateDto
from application.services import comments_service as service
from fastapi import APIRouter, Depends

router = APIRouter(tags=['Comments Router'], prefix="/comments")


@router.post("")
def create_comment(dto: CommentCreateDto,
                   db: Session = Depends(get_db),
                   session_user: Users = Depends(get_session_user)):
    return service.create(dto, db, session_user)


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    # TODO add criteria
    return service.get_all(db)


@router.get("/{id}")
def get(comment_id: int, db: Session = Depends(get_db)):
    return service.get(comment_id, db)


@router.get('/{article_id}')
def get_article_comment(article_id: int, db: Session = Depends(get_db)):
    return service.get_article_comment(article_id, db)


@router.put("")
def update(dto: CommentUpdateDto,
           db: Session = Depends(get_db),
           session_user: Users = Depends(get_session_user)):
    return service.update(dto, db, session_user)


@router.delete("/{id}")
def delete(comment_id: int,
           db: Session = Depends(get_db),
           session_user: Users = Depends(get_session_user)):
    return service.delete(comment_id, db, session_user)
