from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from typing import List
from api.database import get_db
from .models import Administrador, AdministradorDB

route = APIRouter()


# POST /administradores
@route.post(
    "/cria_administradores", response_model=Administrador, tags=["administradores"]
)
def criar_administrador(admin: Administrador, db: Session = Depends(get_db)):
    # Cria um novo administrador sem passar o ID, que será gerado automaticamente
    novo_admin = AdministradorDB(nome=admin.nome, email=admin.email)
    db.add(novo_admin)
    db.commit()
    db.refresh(novo_admin)
    return novo_admin


# GET /administradores/{admin_id}
@route.get(
    "/administradores/{admin_id}",
    response_model=Administrador,
    tags=["administradores"],
)
def obter_administrador(
    admin_id: int = Path(..., title="O ID do administrador a ser obtido"),
    db: Session = Depends(get_db),
):
    admin = db.query(AdministradorDB).filter(AdministradorDB.id == admin_id).first()
    if admin is None:
        raise HTTPException(status_code=404, detail="Administrador não encontrado")
    return admin


# GET /administradores
@route.get(
    "/lista_administradores",
    response_model=List[Administrador],
    tags=["administradores"],
)
def listar_administradores(db: Session = Depends(get_db)):
    administradores = db.query(AdministradorDB).all()
    return administradores


# DELETE /administradores/{admin_id}
@route.delete("/administradores/{admin_id}", tags=["administradores"])
def deletar_administrador(
    admin_id: int = Path(..., title="O ID do administrador a ser deletado"),
    db: Session = Depends(get_db),
):
    admin = db.query(AdministradorDB).filter(AdministradorDB.id == admin_id).first()
    if admin is None:
        raise HTTPException(status_code=404, detail="Administrador não encontrado")
    db.delete(admin)
    db.commit()
    return {"mensagem": "Administrador deletado com sucesso"}
