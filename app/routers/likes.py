from fastapi import APIRouter, status, Depends
from fastapi.exceptions import RequestValidationError, HTTPException
from sqlalchemy.orm import Session

from app.configs.db_config import get_db
from app.entity.entities import Article
from app.schema import like_schema as schema
from app.services import likes as service


class Except(HTTPException):
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail


router = APIRouter(tags=['Likes Router'], prefix="/likes")


@router.post("/{article_id}", status_code=status.HTTP_201_CREATED)
def create(article_id, dto: schema.LikeCreateDto, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()
    if article:
        dto.article_id = article.id
        return service.create(dto, db)
    else:
        raise Except(status_code=status.HTTP_404_NOT_FOUND, detail="Article id Does Not Exist")


@router.put("/{article_id}")
def update(article_id, dto: schema.LikeUpdateDto, db: Session = Depends(get_db)):
    return service.update(dto, article_id, db)

# except Except:
# raise Except(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Article id Does Not Exist")

#
# @router.get("/")
# def get_all(db: Session = Depends(get_db)):
#     return service.get_all(db)
#
#
# @router.get("/{id}", response_model=schema.ArticleDto, responses=_http.get_article)
# def get(id: int, db: Session = Depends(get_db)):
#     return service.get(id, db)
#
#
# @router.put("/")
# def update(dto: schema.ArticleUpdateDto, db: Session = Depends(get_db)):
#     return service.update(dto, db)
#
#
# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def get(id: int, db: Session = Depends(get_db)):
#     return service.delete(id, db)
