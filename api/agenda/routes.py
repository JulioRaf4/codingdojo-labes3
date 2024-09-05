from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import get_db

route = APIRouter()

# Criar novos itens na agenda do evento.

@route.post("./cria_novos_itens", tags=["Agenda"])
def criar_novo_item(db: Session = Depends(get_db)):

    

    db.add(...)
    db.commit()
    db.refresh(...)

    return ...


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

