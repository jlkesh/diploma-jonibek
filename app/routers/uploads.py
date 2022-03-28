from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.configs.db_config import get_db
from app.services import uploads as service
router = APIRouter(tags=['File Uploads'], prefix="/file")

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile, db: Session = Depends(get_db)):
    return await service.create(file, db)
    

# @router.post('/')
# def download_file():
#     pass
