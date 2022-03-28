from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from datetime import datetime

from app import routers
app = FastAPI()

app.include_router(routers.news_router)
app.include_router(routers.likes_router)
app.include_router(routers.articles_router)
app.include_router(routers.comments_router)
app.include_router(routers.users_router)
app.include_router(routers.universities_router)
app.include_router(routers.books_router)
app.include_router(routers.pictures_router)


class  MyException(Exception):
    def __init__(self, message: str) -> None:
        self.message=message


@app.get("/")
def root():
    raise MyException("My custome error raise")
    # return {"data": f"It'is Time {datetime.now()}"}


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    return JSONResponse(content={'error':str(exc)}, status_code=400)


@app.exception_handler(MyException)
def validation_exception_handler(request, exc):
    return JSONResponse(content={'error':str(exc)}, status_code=400)