from fastapi import HTTPException, status
from fastapi.openapi.models import Response
from sqlalchemy.orm import Session

from app.entity.entities import News

from app.schema import news_schema as schema


def create(dto: schema.NewsCreateDto, db: Session):
    news = News(**dto.dict())
    news.created_by = 1
    db.add(news)
    db.commit()
    db.refresh(news)
    return news


def get_all(db: Session):
    return db.query(News).all()


def get(id: int, db: Session):
    news = db.query(News).filter(News.id == id).first()

    if not news:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"News not found with id : '{id}'")

    return news


def update(dto: schema.NewsUpdateDto, db: Session):
    news_query = db.query(News).filter(News.id == dto.id)

    news: News = news_query.first()

    if not news:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article not found with id : '{dto.id}'")

    news_query.update(dto.dict(), synchronize_session=False)

    db.commit()

    return news_query.first()


def delete(id: int, db: Session):
    news_query = db.query(News).filter(News.id == id)

    news: News = news_query.first()

    if not news:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article not found with id : '{id}'")

    news_query.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
