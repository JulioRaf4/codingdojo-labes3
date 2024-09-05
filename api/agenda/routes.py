from fastapi import APIRouter
from .models import Item, Item_criar, ItemDB
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import get_db

route = APIRouter()

# Criar novos itens na agenda do evento.

@route.post("./cria_novos_itens", response_model=Item, tags=["Agenda"])
def criar_novo_item(item: Item_criar, db: Session = Depends(get_db)):

    novo_item = ItemDB(nome=item.nome, data_e_hora = item.data_e_hora, repeticao = item.repeticao)
    
    db.add(novo_item)
    db.commit()
    db.refresh(novo_item)

    return novo_item


# Listar todos os itens da agenda.

@route.get("./listar_itens", tags=["Agenda"])
def listar_itens(db: Session = Depends(get_db)):



    item = db.query(...)

    if item is None:
        raise ...
    return item

# Buscar itens por nome do gestor.

@route.get("./buscar_itens", tags=["Agenda"])
def buscar_item(db: Session = Depends(get_db)):



    item = db.query(...)

    if item is None:
        raise ...
    return item

# Deletar itens da agenda por nome do gestor.

@route.delete("./deletar_itens", tags=["Agenda"])
def deletar_item(db: Session = Depends(get_db)):



    item = db.query(...)

    if item is None:
        raise ...
    db.delete(item)
    db.commit()
    return {"mensagem": "Item deletado com sucesso"}

    return ...
