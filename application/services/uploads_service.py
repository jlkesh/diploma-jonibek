import shutil

from fastapi import UploadFile
from sqlalchemy.orm import Session

from application.configs.oauth2 import has_role
from application.entity.entities import Uploads, Users
from application.utils import join_path, UPLOADS_DIR, generate_new_name


async def create(file: UploadFile, db: Session, session_user: Users):
    has_role(session_user.role, 'ADMIN')
    original_name = file.filename
    generated_name = generate_new_name(original_name)
    content_type = file.content_type
    uploads = Uploads(original_name=original_name,
                      generated_name=generated_name,
                      content_type=content_type,
                      created_by=session_user.id,
                      university_id=session_user.university_id)

    db.add(uploads)
    db.commit()
    db.refresh(uploads)

    with open(join_path(UPLOADS_DIR, generated_name), 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return uploads
