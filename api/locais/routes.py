from http import HTTPStatus
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from .models import LocalSchema, LocalPublic, LocalDB, LocalList, Message
from api.locais.database import get_db


route = APIRouter()


@route.post(
    '/create_local/',
    response_model=LocalPublic,
    status_code=HTTPStatus.CREATED,
)
def create_local(local: LocalSchema, db: Session = Depends(get_db)):
    novo_local = LocalDB(
        nome=local.nome, cidade=local.cidade, estado=local.estado
    )
    db.add(novo_local)
    db.commit()
    db.refresh(novo_local)
    return novo_local


@route.get(
    '/read_locals/', response_model=LocalList, status_code=HTTPStatus.OK
)
def read_locals(db: Session = Depends(get_db)):
    locals = db.query(LocalDB).all()
    return {'locals': locals}


@route.delete(
    '/delete_locals/{local_nome}',
    status_code=HTTPStatus.OK,
    response_model=Message,
)
def delete_local(
    local_nome: str = Path(..., title='O nome do local a ser obtido'),
    db: Session = Depends(get_db),
):
    local = (
        db.query(LocalDB)
        .filter(func.lower(LocalDB.nome) == local_nome.lower())
        .first()
    )
    if local is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Local não encontrado'
        )
    db.delete(local)
    db.commit()
    return {'mensagem': 'Local deletado com sucesso'}


@route.get(
    '/read_local/{local_nome}',
    status_code=HTTPStatus.OK,
    response_model=LocalPublic,
)
def read_local(
    local_nome: str = Path(..., title='O nome do local a ser obtido'),
    db: Session = Depends(get_db),
):
    local = db.query(LocalDB).filter(LocalDB.nome == local_nome).first()
    if local is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Local não encontrado'
        )
    return local
