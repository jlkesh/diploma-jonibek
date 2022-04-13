from fastapi import APIRouter, Depends, HTTPException, UploadFile, status
from fastapi.responses import FileResponse, Response
from sqlalchemy.orm import Session

from application.configs.db_config import get_db
from application.configs.oauth2 import get_session_user, has_role
from application.entity.entities import Uploads, Users
from application.services import uploads_service as service
from application.utils import UPLOADS_DIR

router = APIRouter(tags=['File Uploads'], prefix="/file")


@router.post("")
async def create_upload_file(file: UploadFile,
                             db: Session = Depends(get_db),
                             session_user: Users = Depends(get_session_user)):
    return await service.create(file, db, session_user)


@router.get('/{id}')
async def show_file(filename: str, db: Session = Depends(get_db)):
    upload = db.query(Uploads).filter(Uploads.generated_name == filename).first()
    if not upload:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"File not found with id : '{filename}'")
    return FileResponse(f"{UPLOADS_DIR}/{upload.generated_name}")


@router.get('/download/{id}')
async def download_file(filename: str, db: Session = Depends(get_db)):
    upload = db.query(Uploads).filter(Uploads.generated_name == filename).first()
    if not upload:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"File not found with id : '{filename}'")
    return FileResponse(f"{UPLOADS_DIR}/{upload.generated_name}", media_type=upload.content_type,
                        filename=upload.original_name)


@router.delete("/{id}")
def delete(filename: str, db: Session = Depends(get_db), session_user: Users = Depends(get_session_user)):
    # TODO change users model add extra field for super user
    has_role(session_user.role, 'ADMIN')
    upload_query = db.query(Uploads).filter(Uploads.generated_name == filename)
    upload: Uploads = upload_query.first()
    if not upload:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"File not found with id : '{filename}'")

    if upload.university_id != session_user.university_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'success': True, 'error': 'Forbidden'})
    upload_query.delete(synchronize_session=False)
    return Response(status_code=status.HTTP_204_NO_CONTENT, content="Successfully deleted")
