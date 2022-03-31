from fastapi import APIRouter, Depends, HTTPException, UploadFile, status
from sqlalchemy.orm import Session
from app.entity.entities import Uploads
from app.utils import UPLOADS_DIR
from fastapi.responses import FileResponse
from app.configs.db_config import get_db
from app.services import uploads as service

router = APIRouter(tags=['File Uploads'], prefix="/file")


@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile, db: Session = Depends(get_db)):
    return await service.create(file, db)


def get(id: int, db: Session):
    upload = db.query(Uploads).filter(Uploads.id == id).first()
    if not upload:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"File not found with id : '{id}'")
    return FileResponse(f"{UPLOADS_DIR}/{upload.generated_name}", media_type=upload.content_type,
                        filename=upload.original_name)


@router.get('download/{id}')
async def download_file(id: int, db: Session = Depends(get_db)):
    return get(id=id, db=db)
