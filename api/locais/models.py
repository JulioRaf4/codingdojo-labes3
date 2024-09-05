from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from api.locais.database import Base1


class LocalDB(Base1):
    __tablename__ = 'Locais'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, index=True)
    cidade = Column(String, index=True)
    estado = Column(String, index=True)


class LocalSchema(BaseModel):
    nome: str
    cidade: str
    estado: str


class LocalPublic(BaseModel):
    id: int
    nome: str
    cidade: str
    estado: str


class LocalList(BaseModel):
    locals: list[LocalPublic]


class Message(BaseModel):
    mensagem: str
