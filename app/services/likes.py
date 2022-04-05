from starlette.responses import JSONResponse

from app.schema import like_schema as schema
from app.entity.entities import Book, Article, Like

from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status


def create(dto: schema.LikeCreateDto, db: Session):
    book = Like(**dto.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def update(dto_like: schema.LikeUpdateDto, article_id, db: Session):
    article_query = db.query(Article).filter(Article.id == article_id).first()
    if not article_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article not found with id : '{article_id}'")
    like_query = db.query(Like).filter(Like.id == dto_like.id, Like.article_id == article_query.id)
    like = like_query.first()
    if not like:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Like not found with id : '{id}'")
    like_query.update(dto_like.dict(), synchronize_session=False)
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content="Successfully Updated")
