from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from fastapi.responses import Response

from application.entity.entities import Comment, Article, Users
from application.schema.comment_schema import CommentCreateDto, CommentUpdateDto
from application.services import article_service


def create(dto: CommentCreateDto, db: Session, session_user: Users):
    article_service.get(dto.article_id, db)
    comments = Comment(**dto.dict())
    comments.article_id = dto.article_id
    comments.created_by = session_user.id
    db.add(comments)
    db.commit()
    db.refresh(comments)
    return comments


def update(dto: CommentUpdateDto, db: Session, session_user: Users):
    comment_query = db.query(Comment).filter(Comment.id == dto.comment_id)
    comment = comment_query.first()

    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Comment not found with id : '{dto.comment_id}'")

    if comment.created_by != session_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'error': 'Forbidden'})

    comment_query.update(dto.dict(), synchronize_session=False)
    return Response(content=comment, status_code=status.HTTP_202_ACCEPTED)


def get(comment_id: int, db: Session):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Comment not found with id: '{comment_id}'")
    return Response(status_code=status.HTTP_200_OK, content=comment)


def get_article_comment(article_id: int, db: Session):
    return db.query(Comment).filter(Comment.article_id == article_id).all()


def get_all(db: Session):
    return db.query(Comment).all()


def delete(comment_id: int, db: Session, session_user: Users):
    comment_query = db.query(Comment).filter(Comment.id == comment_id)
    comment = comment_query.first()

    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Comment not found with id: '{comment_id}'")

    if comment.created_by != session_user.id or session_user.role != 'ADMIN':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'error': 'Forbidden'})

    comment_query.delete(synchronize_session=False)
    return Response(status_code=status.HTTP_204_NO_CONTENT, content="Successfully deleted")
