from typing import List, Optional
from fastapi import APIRouter, Header
from pydantic import BaseModel
from fastapi_localization import TranslateJsonResponse, TranslatableStringField

from app.main import app


class LanguageTranslatableSchema(BaseModel):
    language: str
    title: TranslatableStringField


router = APIRouter(tags=['Language Router'], prefix="/locale")


# @app.get("/items/")
# async def read_items():
#     return {"User-Agent": user_agent}

#
# @router.get("/", response_model=List[LanguageTranslatableSchema])
# async def languages(code: Optional[str], text: Optional[str], Accept_Language: Optional[str] = Header(None)):
#     return {"code": code, "message": text, "Accept-Language": Accept_Language, }
