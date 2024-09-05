from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from api.palestrantes.database import Base

class PalestranteDB(Base):
	__tablename__ = "palestrantes"

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	nome = Column(String, index=True)
	assunto = Column(String, index=True)
	cpf = Column(String, unique=True, index=True)

class PalestranteCreate(BaseModel):
	nome: str
	assunto: str
	cpf: str

	class Config:
		from_attributes = True

class Palestrante(BaseModel):
	id: int
	nome: str
	assunto: str
	cpf: str

	class Config:
		from_attributes = True
