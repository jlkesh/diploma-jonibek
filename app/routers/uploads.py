from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.configs.db_config import get_db
from app.services import uploads as service
router = APIRouter(tags=['File Uploads'], prefix="/file")

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile, db):
    await service.create(file)
    return {"filename": file.filename}

# @router.post('/')
# def download_file():
#     pass
