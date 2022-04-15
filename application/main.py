from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from application import routers
from application.configs.db_config import Base, engine
import uvicorn

app = FastAPI()

origins = {
    "http://localhost",
    "http://localhost:3000",
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.news_router)
app.include_router(routers.likes_router)
app.include_router(routers.articles_router)
app.include_router(routers.comments_router)
app.include_router(routers.users_router)
app.include_router(routers.universities_router)
app.include_router(routers.books_router)
app.include_router(routers.pictures_router)
app.include_router(routers.uploads_router)
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    uvicorn.run(app='main:app', port=3000, reload=True)
