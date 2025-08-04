from sqlalchemy import Column, Integer, String, Float, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'
    
    id = Column(Integer, primary_key=True)
    account_number = Column(String(20), unique=True, nullable=False)
    balance = Column(Float, nullable=False, default=0.0)
    status = Column(String(10), nullable=False)
    
    __table_args__ = (
        CheckConstraint(status.in_(('active', 'frozen', 'closed')), name='status_check'),
    )
