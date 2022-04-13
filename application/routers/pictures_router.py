from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from application.configs.db_config import get_db
from application.configs.oauth2 import get_session_user
from application.entity.entities import Users, Picture
from application.schema.pictures_schema import PictureCreateDTO
from application.services import picture_service as service

router = APIRouter(tags=['Picture Router'], prefix="/pictures")


@router.post("")
def create(dto: PictureCreateDTO,
           db: Session = Depends(get_db),
           session_user: Users = Depends(get_session_user)):
    return service.create(dto, db, session_user)


@router.get("")
def get_all(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/{id}")
def get(picture_id: int, db: Session = Depends(get_db)):
    return service.get(picture_id, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(picture_id: int,
           db: Session = Depends(get_db),
           session_user: Users = Depends(get_session_user)):
    return service.delete(picture_id, db, session_user)
