from fastapi import HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from application.entity.entities import Users, University
from application.schema.user_schema import UserCreateDTO, UserLoginDTO, TokenData
from application import utils
from application.configs.oauth2 import generate_access_token


def create(dto: UserCreateDTO, db: Session):
    university = db.query(University).filter(University.id == dto.university_id).first()

    if not university:
        raise HTTPException(
            detail={'error': f'University not found with provided id({dto.university_id})'},
            status_code=status.HTTP_400_BAD_REQUEST)
    user = Users(**dto.dict())
    user.password = utils.encode_password(user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def login(dto: OAuth2PasswordRequestForm, db: Session):
    user = db.query(Users).filter(Users.username == dto.username).first()

    if not user:
        raise HTTPException(
            detail={"error": f"User not found by given username :{dto.username} "},
            status_code=status.HTTP_404_NOT_FOUND)

    if not utils.match_password(dto.password, user.password):
        raise HTTPException(
            detail={'error': 'Invalid credentials'},
            status_code=status.HTTP_400_BAD_REQUEST)
    token = generate_access_token(data={'user_id': user.id})
    return {'access_token': token, "token_type": "Bearer"}


def session_user(db: Session, token_data: TokenData):
    return db.query(Users).filter(Users.id == token_data.id).first()
