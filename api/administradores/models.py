from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from api.database import Base

# Modelo SQLAlchemy para o banco de dados
class AdministradorDB(Base):
    __tablename__ = "administradores"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Modelo Pydantic para validação e conversão de dados
class Administrador(BaseModel):
    id: int = None  # O id será atribuído automaticamente pelo banco de dados
    nome: str
    email: str

    class Config:
        from_attributes = True
