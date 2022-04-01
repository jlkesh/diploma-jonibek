from datetime import datetime
from app.configs.db_config import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from datetime import datetime


# class Auditable(Base):
#     __abstract__ = True
#     created_at: datetime = Column(DateTime, nullable=False, server_default=text('now'))
#     created_by: int = relationship('Users', back_populates='auditable')
#     owner_id: int = Column(ForeignKey('user.id'))
#     is_deleted: bool = Column(Boolean, default=False)


class Article(Base):
    __tablename__ = 'article'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    title: str = Column(String(length=100), nullable=False)
    short: str = Column(String(length=300), index=False, nullable=False)
    body: str = Column(String, nullable=False)
    published: bool = Column(Boolean, server_default='False')
    read_count: int = Column(Integer, server_default='0')
    created_at: datetime = Column(DateTime, nullable=False, server_default='now')
    created_by: int = Column(Integer, ForeignKey('user.id'), nullable=False)

    like = relationship("Like", cascade="all")
    comment = relationship("Comment", cascade="all")


class Uploads(Base):
    __tablename__ = 'uploads'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    original_name: str = Column(String, nullable=False)
    generated_name: str = Column(String, nullable=False)
    content_type: str = Column(String, nullable=False)
    created_at: datetime = Column(DateTime, nullable=False, server_default='now')
    created_by: int = Column(Integer, ForeignKey('user.id'), nullable=False)


class Book(Base):
    __tablename__ = 'books'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    name: str = Column(String(length=300), index=False)
    author: str = Column(String, nullable=False, index=True)
    short_info: str = Column(String)
    page_count: int = Column(Integer, server_default='0')

    created_at: datetime = Column(DateTime, nullable=False, server_default='now')
    created_by: int = Column(Integer, ForeignKey('user.id'), nullable=False)


class Users(Base):
    __tablename__ = 'user'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    username: str = Column(String(length=100), index=False)
    password: str = Column(String(length=300))
    university_id: int = Column(Integer, ForeignKey('university.id'))
    is_active: bool = Column(Boolean, server_default='True')
    role: str = Column(String, default='employee', server_default='employee')
    created_at: datetime = Column(DateTime, nullable=False, server_default='now')


class University(Base):
    __tablename__ = 'university'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    name: str = Column(String(length=200))
    abbr: str = Column(String(length=10))
    description: str = Column(String(length=500))
    created_at: datetime = Column(DateTime, nullable=False, server_default='now')
    created_by: int = Column(Integer, nullable=False, server_default='-1')


class News(Base):
    __tablename__ = 'news'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    title: str = Column(String(300))
    body: str = Column(String)
    created_at: datetime = Column(DateTime, nullable=False, server_default='now')
    created_by: int = Column(Integer, ForeignKey('user.id'), nullable=False)


class Like(Base):
    __tablename__ = 'like'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    is_like: bool = Column(Boolean, nullable=False)
    article_id: int = Column(Integer, ForeignKey('article.id'))
    created_at = Column(DateTime, nullable=False, server_default='now')


class Comment(Base):
    __tablename__ = 'comment'
    id: int = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    message: str = Column(String(100))
    article_id: int = Column(Integer, ForeignKey('article.id'))

    created_at: datetime = Column(DateTime, nullable=False, server_default='now')
    created_by: int = Column(Integer, ForeignKey('user.id'), nullable=False)
