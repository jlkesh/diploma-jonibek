from datetime import datetime
from email.policy import default
from app.configs.db_config import Base
from sqlalchemy import Column,Integer,String,DateTime,Boolean
from sqlalchemy.sql.expression import text


class Article(Base):
    __tablename__ = 'article'
    id: int = Column(Integer,primary_key = True, unique = True, index = True, nullable=False)
    title: str = Column(String( length=100), nullable=False)
    short: str = Column(String(length=300), index=False)
    description: int = Column(Integer, nullable=False)
    published: str = Column(Boolean, server_default='False')
    read_count: int = Column(Integer, server_default='0')
    created_at: datetime = Column(DateTime, nullable=False, server_default=text('now'))

