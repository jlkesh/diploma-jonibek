from fastapi import APIRouter, Depends, status

from application.configs.oauth2 import get_session_user
from application.entity.entities import Users
from application.services import universities_service as service
from application.schema import universities_schema as schema
from sqlalchemy.orm import Session
from application.configs.db_config import get_db
from application import http_response

router = APIRouter(tags=['University Router'], prefix="/university")


@router.post("", status_code=status.HTTP_201_CREATED)
def create(dto: schema.UniversityCreateDto,
           db: Session = Depends(get_db),
           session_user: Users = Depends(get_session_user)):
    return service.create(dto, db, session_user)


@router.get("")
def get_all(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/{id}", response_model=schema.UniversityDto, responses=http_response.get_university)
def get(university_id: int,
        db: Session = Depends(get_db),
        session_user: Users = Depends(get_session_user)):
    return service.get(university_id, db, session_user)


@router.put("")
def update(dto: schema.UniversityUpdateDto,
           db: Session = Depends(get_db),
           session_user: Users = Depends(get_session_user)):
    return service.update(dto, db, session_user)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def get(university_id: int,
        db: Session = Depends(get_db),
        session_user: Users = Depends(get_session_user)):
    return service.delete(university_id, db, session_user)
