from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schema.user_schema import AuthUserCreateDTO
from app.entity.entities import Users, University


def create(dto: AuthUserCreateDTO,db: Session):
    university = db.query(University).filter(University.id == dto.university_id).first()
    if not university:
        raise  HTTPException(
            detail={'error':f'University not found with provided id({dto.university_id})'},
            status_code=status.HTTP_400_BAD_REQUEST)

    user = Users(**dto.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

