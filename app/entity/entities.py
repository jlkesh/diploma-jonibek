from datetime import datetime
from email.policy import default
from app.configs.db_config import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

ROLE_CHOICE = (
    ('admin', "ADMIN"),
)


class Article(Base):
    __tablename__ = 'article'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    title: str = Column(String(length=100), nullable=False)
    short: str = Column(String(length=300), index=False)
    description: int = Column(Integer, nullable=False)
    published: str = Column(Boolean, server_default='False')
    read_count: int = Column(Integer, server_default='0')
    like = relationship("Like", back_populates='article')
    comment = relationship("Comment", back_populates='article')
    created_at: datetime = Column(DateTime, nullable=False, server_default=text('now'))


class Uploads(Base):
    __tablename__ = 'uploads'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    original_name = Column(String, nullable=False)
    generated_name = Column(String, nullable=False)
    content_type = Column(String, nullable=False)
    path = Column(String, nullable=False)


class Book(Base):
    __tablename__ = 'books'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    name: str = Column(String(length=300), index=False)
    author: int = Column(Integer, nullable=False)
    short_info: str = Column(Boolean, server_default='False')
    page_count: int = Column(Integer, server_default='0')
    created_at: datetime = Column(DateTime, nullable=False, server_default=text('now'))
    created_by: datetime = Column(DateTime, nullable=False, server_default=text('now'))
    # file = relationship('Uploads')


class Users(Base):
    __tablename__ = 'user'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    username: str = Column(String(length=100), index=False)
    password: str = Column(String(length=300))
    university_id: str = Column(Integer, ForeignKey('university.id'))
    is_active: bool = Column(Boolean, server_default='True')
    role: str = Column(String, default='employee', server_default='employee')


class University(Base):
    __tablename__ = 'university'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    name: str = Column(String(length=200))
    user = relationship('Users', back_populates='university')
    # rating: int = Column()


class News(Base):
    __tablename__ = 'news'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    title: str = Column(String(300))
    body: str = Column(String)
    # uploads_news:int=


class Like(Base):
    __tablename__ = 'like'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    like: bool = Column(Boolean, default=False)
    dis_like: bool = Column(Boolean, default=False)
    article = relationship('Article', back_populates='like')
    article_id: int = Column(Integer, ForeignKey('article.id'))


class Comment(Base):
    __tablename__ = 'comment'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    title: str = Column(String(100))
    body: str = Column(String(500))
    article = relationship('Article', back_populations='comment')
    article_id = Column(Integer, ForeignKey('article.id'))
