from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from application.configs.db_config import get_db
from application.configs.oauth2 import get_session_user
from application.schema.user_schema import UserCreateDTO, TokenData, UserDTO
from application.services import users_service as service

router = APIRouter(tags=['Users Router'], prefix="/users")


@router.post('/create')
def user_create(dto: UserCreateDTO, db: Session = Depends(get_db)):
    return service.create(dto=dto, db=db)


@router.post('/login')
def login(dto: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return service.login(dto, db)


@router.get('/me', response_model=UserDTO)
def login(db: Session = Depends(get_db), session_user: TokenData = Depends(get_session_user)):
    return service.session_user(db, session_user)
