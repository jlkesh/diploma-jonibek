from app.dto import articles as schema
from app.entity.entities import Article


from sqlalchemy.orm import Session

from fastapi.responses import UJSONResponse
from fastapi.exceptions import HTTPException
from fastapi import Response, status


def create(dto: schema.ArticleCreateDto, db: Session):
    article = Article(**dto.dict())
    article.created_by = 1
    db.add(article)
    db.commit()
    db.refresh(article)
    return article
    

def get_all(db: Session ):
    return db.query(Article).all()



def get(id: int, db: Session ):
    
    article = db.query(Article).filter(Article.id == id).first()
    
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article not found with id : '{id}'")

    return article




def update(dto: schema.ArticleUpdateDto, db: Session ):
    
    article_query = db.query(Article).filter(Article.id == dto.id)
    
    article: Article = article_query.first()
    
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article not found with id : '{dto.id}'")    
    
    article_query.update(dto.dict(), synchronize_session=False)
    
    db.commit()

    return article_query.first()



def delete(id: int, db: Session ):
    
    article_query = db.query(Article).filter(Article.id == id)
    
    article: Article = article_query.first()
    
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article not found with id : '{id}'")    
    
    article_query.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)




