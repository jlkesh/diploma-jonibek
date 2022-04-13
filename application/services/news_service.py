from fastapi import HTTPException, status
from fastapi.openapi.models import Response
from sqlalchemy.orm import Session

from application.configs.oauth2 import has_role
from application.entity.entities import News, Users

from application.schema import news_schema as schema


def create(dto: schema.NewsCreateDto, db: Session, session_user: Users):
    has_role(session_user.role, 'ADMIN')
    news = News(created_by=session_user.id, university_id=session_user.university_id, **dto.dict())
    db.add(news)
    db.commit()
    db.refresh(news)
    return news


def get_all(db: Session):
    return db.query(News).all()


def get(news_id: int, db: Session):
    news = db.query(News).filter(News.id == news_id).first()

    if not news:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"News not found with id : '{news_id}'")

    return news


def update(dto: schema.NewsUpdateDto, db: Session, session_user: Users):

    has_role(session_user.role, 'ADMIN')
    news_query = db.query(News).filter(News.id == dto.id)
    news: News = news_query.first()

    if not news:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article not found with id : '{dto.id}'")

    if news.university_id != session_user.university_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'success': False, 'error': 'Forbidden'})

    news_query.update(dto.dict(), synchronize_session=False)

    db.commit()

    return news_query.first()


def delete(news_id: int, db: Session, session_user: Users):
    has_role(session_user.role, 'ADMIN')
    news_query = db.query(News).filter(News.id == news_id)
    news: News = news_query.first()

    if not news:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article not found with id : '{news_id}'")

    if news.university_id != session_user.university_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'success': False, 'error': 'Forbidden'})

    news_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
