from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from typing import List
from api.participantes.database import get_db
from .models import ParticipantCreate, Participant, ParticipantDB

route = APIRouter()

# GET /participant/getAll
@route.get("/participant/getAll", response_model=List[Participant], tags=["participant"],)
def get_all_participants(db: Session = Depends(get_db)):
    participants = db.query(ParticipantDB).all()
    return participants

# GET /participant/getByCpf
@route.get("/participant/getByCpf", response_model=Participant, tags=["participant"],)
def get_participant_by_cpf(cpf: str, db: Session = Depends(get_db)):
    participant = db.query(ParticipantDB).filter(ParticipantDB.cpf == cpf).first()
    
    if participant is None:
        raise HTTPException(status_code=404, detail="Participante com esse cpf não foi encontrado")
    return participant

# POST /participant/create
@route.post("/participant/create", response_model=ParticipantCreate, tags=["participant"],)
def create_participant(participant: ParticipantCreate, db: Session = Depends(get_db)):
    
    # Verifica se o email já existe no banco de dados
    db_participant = db.query(ParticipantDB).filter(ParticipantDB.cpf == participant.cpf).first()
    
    if db_participant:
        raise HTTPException(status_code=400, detail="CPF já cadastrado")
    
    novo_participant = ParticipantDB(name=participant.name, date_of_birth=participant.date_of_birth, cpf=participant.cpf)
    db.add(novo_participant)
    db.commit()
    db.refresh(novo_participant)
    return novo_participant

# DELETE /participant/deleteByCpf
@route.delete("/participant/deleteByCpf", tags=["participant"],)
def delete_participant_by_cpf(cpf: str, db: Session = Depends(get_db)):
    participant = db.query(ParticipantDB).filter(ParticipantDB.cpf == cpf).first()
    
    if participant is None:
        raise HTTPException(status_code=404, detail="Participante com esse cpf não foi encontrado")
    
    db.delete(participant)
    db.commit()
    return {"mensagem": "Participante deletado com sucesso"}