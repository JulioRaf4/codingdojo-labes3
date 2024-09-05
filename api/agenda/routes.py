from fastapi import APIRouter
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import get_db
from .models import ItemCreate, ItemResponse, ItemDB
from fastapi import HTTPException

route = APIRouter()

# Criar novos itens na agenda do evento.

@route.post("./cria_novos_itens", response_model=ItemResponse, tags=["Agenda"])
def criar_novo_item(item: ItemCreate, db: Session = Depends(get_db)):

    novo_item = ItemDB(nome=item.nome, data_e_hora = item.data_e_hora, repeticao = item.repeticao)
    
    db.add(novo_item)
    db.commit()
    db.refresh(novo_item)

    return novo_item


# Listar todos os itens da agenda
@route.get("/listar_itens", response_model=list[ItemResponse], tags=["Agenda"])
def listar_itens(db: Session = Depends(get_db)):
    itens = db.query(ItemDB).all()
    if not itens:
        raise HTTPException(status_code=404, detail="Nenhum item encontrado")
    return itens

# Buscar itens por nome do gestor
@route.get("/buscar_itens", response_model=list[ItemResponse], tags=["Agenda"])
def buscar_item(nome: str, db: Session = Depends(get_db)):
    item = db.query(ItemDB).filter(ItemDB.nome == nome)
    if item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item

# Deletar itens da agenda por nome do gestor.

@route.delete("./deletar_itens/{item_id}", tags=["Agenda"])
def deletar_item(item_id: int, db: Session = Depends(get_db)):

    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()

    if item is None:
        raise HTTPException(status_code=404, detail="Não existe nenhum item com esse id")

    
    db.delete(item)
    db.commit()
    return {"mensagem": "Item deletado com sucesso"}    

