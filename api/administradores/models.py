from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from api.database import Base


# Modelo SQLAlchemy para o banco de dados
class AdministradorDB(Base):
    __tablename__ = 'administradores'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)


# Modelo Pydantic para conversão de dados (sem ID para criação)
class AdministradorCreate(BaseModel):
    nome: str
    email: str

    class Config:
        from_attributes = True


# Modelo Pydantic para retorno de dados (com ID)
class Administrador(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True
