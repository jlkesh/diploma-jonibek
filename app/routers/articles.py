from fastapi import APIRouter

from app.services import article_service
from app.dto import articles

router = APIRouter(tags=['Article Router'], prefix="/articles")


@router.post("/")
def create(dto: articles.ArticleCreateDto):
    return article_service.create(dto)


@router.get("/")
def get_all():
    return article_service.get_all()


@router.get("/{id}")
def get(id: int):
    pass



@router.put("/{id}")
def get(id: int):
    pass


@router.delete("/{id}")
def get(id: int):
    pass







