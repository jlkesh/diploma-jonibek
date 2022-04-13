from fastapi import Response, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from application.configs.oauth2 import has_role
from application.entity.entities import University, Users
from application.schema import universities_schema as schema


def create(dto: schema.UniversityCreateDto, db: Session, session_user: Users):
    has_role(session_user.role, 'SUPER_ADMIN')
    university = University(**dto.dict())
    university.created_by = session_user.id
    db.add(university)
    db.commit()
    db.refresh(university)
    return university


def get_all(db: Session):
    return db.query(University).all()


def get(university_id: int, db: Session, session_user: Users):
    if session_user.university_id != university_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'success': False, 'error': 'Forbidden'})

    book = db.query(University).filter(University.id == university_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Article not found with id : '{university_id}'")

    return book


def update(dto: schema.UniversityUpdateDto, db: Session, session_user: Users):
    has_role(session_user, 'ADMIN')
    has_role(session_user, 'SUPER_ADMIN')
    university_query = db.query().filter(University.id == dto.id)
    university: University = university_query.first()

    if not university:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book not found with id : '{id}'")

    if session_user.role == 'ADMIN' and dto.id != session_user.university_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'success': True, 'error': 'Forbidden'})

    university.update(dto.dict(), synchronize_session=False)
    db.commit()
    return True


def delete(university_id: int, db: Session, session_user: Users):
    has_role(session_user, 'ADMIN')
    has_role(session_user, 'SUPER_ADMIN')
    university_query = db.query(University).filter(University.id == university_id)
    university: University = university_query.first()

    if not university:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Article not found with id : {university_id}")

    if session_user.role == 'ADMIN' and university_id != session_user.university_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'success': True, 'error': 'Forbidden'})

    university_query.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
