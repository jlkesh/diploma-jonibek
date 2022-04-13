from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from application.configs.db_config import get_db
from application.configs.oauth2 import get_session_user
from application.entity.entities import Users
from application.schema import like_schema as schema
from application.services import likes_service as service

router = APIRouter(tags=['Likes Router'], prefix="/likes")


@router.post("")
def create(dto: schema.LikeCreateDto,
           db: Session = Depends(get_db),
           session_user: Users = Depends(get_session_user)):
    return service.create(dto, db, session_user)

# @router.put("")
# def update(dto: schema.LikeUpdateDto,
#            db: Session = Depends(get_db),
#            session_user: Users = Depends(get_session_user)):
#     return service.update(dto, db, session_user)

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
