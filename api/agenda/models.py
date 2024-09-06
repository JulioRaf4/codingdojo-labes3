from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from api.database import Base

# Modelo Pydantic para criação de novos itens
class ItemCreate(BaseModel):
    nome: str
    data_e_hora: str
    repeticao: str

# Modelo Pydantic para a resposta
class ItemResponse(BaseModel):
    id: int
    nome: str
    data_e_hora: str
    repeticao: str

    class Config:
        orm_mode = True  # Permite a conversão de modelos SQLAlchemy para Pydantic


# Modelo SQLAlchemy para o banco de dados
class ItemDB(Base):
    __tablename__ = "Item"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, index=True)
    data_e_hora = Column(String, index=True)
    repeticao = Column(String, index=True)