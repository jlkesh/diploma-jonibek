from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.entity.entities import Comment, Article
from app.schema.comment_schema import CommentCreateDto, CommentUpdateDto


def create(article_id, dto: CommentCreateDto, db: Session):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article not found with id: {article_id}")
    comments = Comment(**dto.dict())
    comments.article_id = article_id
    comments.created_by = 4
    db.add(comments)
    db.commit()
    db.refresh(comments)
    return comments


def update(id: int, dto: CommentUpdateDto, db: Session):
    comment_query = db.query(Comment).filter(Comment.id == id)
    comment = comment_query.first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Comment not found with id : '{id}'")
    comment_query.update(dto.dict(), synchronize_session=False)
    return Response(content=comment, status_code=status.HTTP_202_ACCEPTED)


def get(id: int, db: Session):
    comment = db.query(Comment).filter(Comment.id == id).first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Comment not found with id: '{id}'")
    return Response(status_code=status.HTTP_200_OK, content=comment)


def get_article_comment(article_id: int, db: Session):
    return db.query(Comment).filter(Comment.article_id == article_id).all()


def get_all(db: Session):
    return db.query(Comment).all()


def delete(id: int, db: Session):
    comment_query = db.query(Comment).filter(Comment.id == id)
    comment = comment_query.first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Comment not found with id: '{id}'")
    comment_query.delete(synchronize_session=False)
    return Response(status_code=status.HTTP_204_NO_CONTENT, content="Successfully deleted")
