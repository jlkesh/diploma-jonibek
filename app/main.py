import http.client
import uvicorn
from fastapi import FastAPI
from datetime import datetime
from app import routers
from app.configs.db_config import Base, engine

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
app.include_router(routers.download_router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"data": f"It'is Time {datetime.now()}"}


if __name__ == '__main__':
    uvicorn.run('main:app')
