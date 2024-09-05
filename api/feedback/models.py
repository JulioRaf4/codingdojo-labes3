from sqlalchemy import Column, Integer, String, Date
from pydantic import BaseModel
from .database import Base

from datetime import date

class FeedbackDB(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    avaliacao = Column(Integer, nullable=False)
    descricao = Column(String, nullable=False)
    data = Column(Date)

class FeedbackCreate(BaseModel):
    avaliacao: int
    descricao: str
    data: date  

    class Config:
        from_attributes = True

class Feedback(BaseModel):
    id: int
    avaliacao: int
    descricao: str
    data: date
    class Config:
        from_attributes = True
