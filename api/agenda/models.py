from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from api.database import Base


class Item(BaseModel):
    id: int
    nome: str
    data_e_hora: str
    repeticao: str

class Item_criar(BaseModel):
    nome: str
    data_e_hora: str
    repeticao: str



# Modelo SQLAlchemy para o banco de dados
class ItemDB(Base):
    __tablename__ = "Item"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, index=True)
    data_e_hora = Column(String, index=True)
    repeticao = Column(String, index=True)