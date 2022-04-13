from fastapi import HTTPException, Response
from sqlalchemy.orm import Session
from starlette import status

from application.configs.oauth2 import has_role
from application.entity.entities import Users, Picture
from application.schema.pictures_schema import PictureCreateDTO


def create(dto: PictureCreateDTO, db: Session, session_user: Users):
    picture = Picture(university_id=session_user.university_id, created_by=session_user.id, **dto.dict())
    db.add(Picture)
    db.commit()
    db.refresh(picture)
    return picture


def get_all(db: Session):
    return db.query(Picture).all()


def get(picture_id, db: Session):
    picture = db.query(Picture).filter(Picture.id == picture_id).first()
    if not picture:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Picture not found with id : '{picture_id}'")
    return picture


def delete(picture_id: int, db: Session, session_user: Users):
    has_role(session_user.role, 'ADMIN')

    picture_query = db.query(Picture).filter(Picture.id == picture_id)
    picture: Picture = picture_query.first()

    if not picture:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Picture not found with id : '{picture_id}'")

    if picture.university_id != session_user.university_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'error': 'Forbidden'})

    picture_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
