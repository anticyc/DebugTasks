import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, nullable=False, unique=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    info = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now())

def create_db():
    db = sa.create_engine(url="sqlite:///:memory:", connect_args={"check_same_thread": False})
    Base.metadata.drop_all(db)
    session_maker = sessionmaker(bind=db)
    Base.metadata.create_all(db)
    return session_maker
