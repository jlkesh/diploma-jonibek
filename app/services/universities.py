from app.dto import universities as schema
from app.entity.entities import University
from sqlalchemy.orm import Session

from fastapi.responses import UJSONResponse
from fastapi.exceptions import HTTPException
from fastapi import Response, status



def create(dto: schema.UniversityCreateDto, db: Session):
    university = University(**dto.dict())
    db.add(university)
    db.commit()
    db.refresh(university)
    return university


def get_all(db: Session):
    return db.query(University).all()


def get(id: int, db: Session):
    book = db.query(University).filter(University.id == id).first()

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article not found with id : '{id}'")

    return book


def update(dto: schema.UniversityUpdateDto, db: Session):
    university_query = db.query().filter(University.id == dto.id)

    university: University = university_query.first()

    if not university:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book not found with id : '{id}'")

    university.update(dto.dict(), synchronize_session=False)

    db.commit()

    return True


def delete(id: int, db: Session):
    university_query = db.query(University).filter(University.id == id)

    university: University = university_query.first()

    if not university:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article not found with id : '{id}'")

    university_query.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
