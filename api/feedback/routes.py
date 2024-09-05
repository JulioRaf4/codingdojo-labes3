from datetime import datetime, date
from api.database import get_db
from .models import FeedbackDB, FeedbackCreate, Feedback
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from typing import List

route = APIRouter()

def string_para_data(data_str):
    if isinstance(data_str, str):
        return datetime.strptime(data_str, "%Y-%m-%d").date()
    elif isinstance(data_str, date):
        return data_str
    else:
        raise TypeError("O argumento deve ser uma string ou um objeto datetime.date")

@route.post("/cria_feedback", response_model=Feedback, tags=["feedbacks"])
def criar_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    # Converte a data de string para date
    data_formatada = string_para_data(feedback.data)
    
    novo_feedback = FeedbackDB(
        avaliacao=feedback.avaliacao,
        descricao=feedback.descricao,
        data=data_formatada
    )
    db.add(novo_feedback)
    db.commit()
    db.refresh(novo_feedback)
    return novo_feedback

@route.get("/get_feedback/{feedback_id}", response_model=Feedback, tags=["feedbacks"])
def obter_feedback(
    feedback_id: int = Path(..., title="O ID do feedback a ser obtido"),
    db: Session = Depends(get_db),
):
    feedback = db.query(FeedbackDB).filter(FeedbackDB.id == feedback_id).first()
    if feedback is None:
        raise HTTPException(status_code=404, detail="Feedback não encontrado")
    return feedback

@route.get("/get_feedbacks", response_model=List[Feedback], tags=["feedbacks"])
def listar_feedbacks(db: Session = Depends(get_db)):
    feedbacks = db.query(FeedbackDB).all()
    return feedbacks

@route.delete("/delete_feedback/{feedback_id}", tags=["feedbacks"])
def deletar_feedback(
    feedback_id: int = Path(..., title="O ID do feedback a ser deletado"),
    db: Session = Depends(get_db),
):
    feedback = db.query(FeedbackDB).filter(FeedbackDB.id == feedback_id).first()
    if feedback is None:
        raise HTTPException(status_code=404, detail="Feedback não encontrado")
    db.delete(feedback)
    db.commit()
    return {"mensagem": "Feedback deletado com sucesso"}
