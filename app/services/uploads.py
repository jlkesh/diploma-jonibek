from fastapi import UploadFile
from sqlalchemy.orm import Session
import shutil
from app.utils import join_path, UPLOADS_DIR, unique_code, get_extension, generate_new_name

async def create(file: UploadFile, db: Session):
    original_name = file.filename
    generated_name = generate_new_name(original_name)
    content_type = file.content_type
    path = join_path('uploads', generated_name)

    with open(join_path(UPLOADS_DIR, generated_name),'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
        
