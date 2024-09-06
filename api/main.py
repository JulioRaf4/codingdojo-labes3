from api.participantes.routes import route as rota_participant
from api.participantes.database import Base, engine
from api.database import Base, engine
from api.administradores.routes import route as rota_administrador
from api.feedback.routes import route as rota_feedback
from fastapi import FastAPI
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Coding Dojo")


app.include_router(rota_participant, prefix="/api")
app.include_router(rota_administrador, prefix="/api")
app.include_router(rota_feedback, prefix="/api_feedback")

if __name__ == "__main__":
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True)
