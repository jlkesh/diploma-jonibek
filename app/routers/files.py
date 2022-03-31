from fastapi import APIRouter, Depends, UploadFile, HTTPException, status
from fastapi.responses import FileResponse
from fastapi import APIRouter, Depends, HTTPException, UploadFile, status
from sqlalchemy.orm import Session
from app.entity.entities import Uploads
from app.utils import UPLOADS_DIR
from fastapi.responses import FileResponse
from app.configs.db_config import get_db
from app.services import uploads as service
from app.utils import UPLOADS_DIR

router = APIRouter(tags=['File Uploads'], prefix="/file")


@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile, db: Session = Depends(get_db)):
    return await service.create(file, db)


@router.get('download/{id}')
async def download_file(id: int, db: Session = Depends(get_db)):
    upload = db.query(Uploads).filter(Uploads.id == id).first()
    from app.entity.entities import Uploads
    if not upload:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"File not found with id : '{id}'")
    return FileResponse(f"{UPLOADS_DIR}/{upload.generated_name}", media_type=upload.content_type,
                        filename=upload.original_name)
