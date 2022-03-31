from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.configs.db_config import get_db
from app.schema.user_schema import AuthUserCreateDTO
from app.services import users_service as service

router = APIRouter(tags=['Users Router'], prefix="/users")


@router.post("/")
def create(dto: AuthUserCreateDTO, db: Session =  Depends(get_db)):
    return service.create(dto, db)


@router.get("/")
def get_all():
    pass


@router.get("/{id}")
def get(id: int):
    pass



@router.put("/{id}")
def update(id: int):
    pass


@router.delete("/{id}")
def delete(id: int):
    pass







