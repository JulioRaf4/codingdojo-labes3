from pydantic import BaseModel

class Item(BaseModel):
    id: int
    nome: str
    data_e_hora: str
    repeticao: str

class Item_criar(BaseModel):
    nome: str
    data_e_hora: str
    repeticao: str
