from app.dto.articles import ArticleCreateDto
from sqlalchemy.orm import Session
from fastapi import Depends
from . import get_db
from app.entity.entities import Article


def create(dto: ArticleCreateDto, db:Session = Depends(get_db)):
    article = Article(**dto.dict())
    db.add(article)
    db.commit()
    db.refresh(article)
    

def get_all(db:Session = Depends(get_db)):
    return db.query(Article).all()


