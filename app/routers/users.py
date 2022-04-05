from datetime import timedelta

from app.entity.entities import Users
from app.schema.user_schema import AuthUserCreateDTO
from app.services import users_service as service
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.configs.db_config import get_db
from app.services.users_service import get_current_user, authenticate, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, \
    Token

router = APIRouter(tags=['Users Router'], prefix="/users")


@router.post('/')
async def user_create(dto: AuthUserCreateDTO, db: Session = Depends(get_db)):
    return await service.create(dto=dto, db=db)


@router.get("/detail")
async def user_detail(current_user: Users = Depends(get_current_user)):
    return {"name": "Danny", "email": "danny@tutorialsbuddy.com"}


@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    if authenticate(username, password):
        access_token = create_access_token(
            data={"sub": username}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
