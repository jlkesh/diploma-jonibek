from fastapi import UploadFile
from sqlalchemy.orm import Session
import shutil
from app.utils import join_path, UPLOADS_DIR, unique_code, get_extension, generate_new_name
from app.entity.entities import Uploads


async def create(file: UploadFile, db: Session):
    original_name = file.filename
    generated_name = generate_new_name(original_name)
    content_type = file.content_type
    path = join_path('uploads', generated_name)
    uploads = Uploads(original_name=original_name, generated_name=generated_name, content_type=content_type, path=path)
    db.add(uploads)
    db.commit()
    db.refresh(uploads)

    with open(join_path(UPLOADS_DIR, generated_name), 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return uploads
