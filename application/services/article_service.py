from fastapi import Response, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from application.configs.oauth2 import has_role
from application.entity.entities import Article, Users
from application.schema import article_schema as schema


def create(dto: schema.ArticleCreateDto, db: Session, session_user: Users):
    has_role(session_user.role, 'ADMIN')
    article = Article(**dto.dict())
    article.created_by = session_user.id
    article.university_id = session_user.university_id
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def get_all(db: Session):
    return db.query(Article).all()


def get(article_id: int, db: Session):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article not found with id : '{article_id}'")
    return article


def update(dto: schema.ArticleUpdateDto, db: Session, session_user=Users):

    has_role(session_user.role, 'ADMIN')

    article_query = db.query(Article).filter(Article.id == dto.id)
    article: Article = article_query.first()

    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article not found with id : '{dto.id}'")

    if article.university_id != session_user.university_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'error': 'Forbidden'})

    article_query.update(dto.dict(), synchronize_session=False)

    db.commit()

    return article_query.first()


def delete(article_id: int, db: Session, session_user: Users):

    has_role(session_user.role, 'ADMIN')

    article_query = db.query(Article).filter(Article.id == article_id)
    article: Article = article_query.first()

    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article not found with id : '{article_id}'")

    if article.university_id != session_user.university_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'error': 'Forbidden'})

    article_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
