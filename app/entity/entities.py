from datetime import datetime
from email.policy import default
from app.configs.db_config import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class Article(Base):
    __tablename__ = 'article'
    id: int = Column(Integer,primary_key = True, unique = True, index = True, nullable=False)
    title: str = Column(String( length=100), nullable=False)
    short: str = Column(String(length=300), index=False)
    description: int = Column(Integer, nullable=False)
    published: str = Column(Boolean, server_default='False')
    read_count: int = Column(Integer, server_default='0')
    created_at: datetime = Column(DateTime, nullable=False, server_default=text('now'))

class Uploads(Base):
    __tablename__ = 'uploads'
    id: int = Column(Integer,primary_key = True, unique = True, index = True, nullable=False)
    original_name = Column(String, nullable=False)
    generated_name = Column(String, nullable=False)
    content_type = Column(String, nullable=False)
    path = Column(String, nullable=False)

class Book(Base):
    __tablename__ = 'books'
    id: int = Column(Integer,primary_key = True, unique = True, index = True, nullable=False)
    name: str = Column(String(length=300), index=False)
    author: int = Column(Integer, nullable=False)
    short_info: str = Column(Boolean, server_default='False')
    page_count: int = Column(Integer, server_default='0')
    created_at: datetime = Column(DateTime, nullable=False, server_default=text('now'))
    created_by: datetime = Column(DateTime, nullable=False, server_default=text('now'))
    file = relationship('Uploads')

