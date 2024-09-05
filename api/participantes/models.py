from sqlalchemy import Date, Column, Integer, String
from pydantic import BaseModel
from datetime import date  # Para Pydantic
from .database import Base

class ParticipantDB(Base): 
    __tablename__ = "participantes"
    
    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    date_of_birth = Column(Date, index=True, nullable=False)
    cpf = Column(String, index=True, nullable=False, unique=True)

# Pydantic models
class ParticipantCreate(BaseModel):
    name: str
    date_of_birth: date  
    cpf: str
    
    class Config:
        from_attributes = True
        
class Participant(BaseModel):
    id: int
    name: str
    date_of_birth: date  
    cpf: str
    
    class Config:
        from_attributes = True
