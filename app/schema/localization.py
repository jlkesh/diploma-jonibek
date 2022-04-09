from typing import List
from pydantic import BaseModel
from fastapi_localization import TranslateJsonResponse
from fastapi_localization import TranslatableStringField


class LanguageTranslatableSchema(BaseModel):
    code: str
    title: TranslatableStringField
