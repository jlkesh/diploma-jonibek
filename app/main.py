import uvicorn
from fastapi import FastAPI, Header
from fastapi.exceptions import RequestValidationError
from datetime import datetime

from fastapi_localization import TranslateJsonResponse
from starlette.middleware.cors import CORSMiddleware

from app import routers
from app.configs.db_config import Base, engine
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)

from app.schema.localization import LanguageTranslatableSchema

app = FastAPI()
app.include_router(routers.news_router)
app.include_router(routers.likes_router)
app.include_router(routers.articles_router)
app.include_router(routers.comments_router)
app.include_router(routers.users_router)
app.include_router(routers.universities_router)
app.include_router(routers.books_router)
app.include_router(routers.pictures_router)
app.include_router(routers.uploads_router)
app.include_router(routers.exception_handler_router)
# app.include_router(routers.locale_router)
Base.metadata.create_all(bind=engine)
origins = [
    'http://localhost:3000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET'],
    allow_headers=['Content-Type', 'application/xml'],
)


@app.get("/")
def root():
    return {"data": f"It'is Time {datetime.now()}"}


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    # print(f"OMG! An HTTP error!: {repr(exc)}")
    return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    # print(f"OMG! The client sent invalid data!: {exc}")
    return await request_validation_exception_handler(request, exc)


if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=2001)
