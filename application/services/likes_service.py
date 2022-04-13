from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from application.entity.entities import Article, Like, Users
from application.schema import like_schema as schema


def create(dto: schema.LikeCreateDto, db: Session, session_user: Users):
    article = db.query(Article).filter(Article.id == dto.article_id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'error': 'Article not found'})

    like_query = db.query(Like).filter(Like.created_by == session_user.id, Like.article_id == dto.article_id)
    like = like_query.first()

    if like:
        like_query.update(dto.dict(), synchronize_session=False)
        db.commit()
        return JSONResponse(status_code=status.HTTP_200_OK, content={'success': True})

    like = Like(created_by=session_user.id, **dto.dict())
    db.add(like)
    db.commit()
    db.refresh(like)
    return like
