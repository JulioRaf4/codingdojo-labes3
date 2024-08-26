from fastapi import FastAPI
from api.administradores.routes import route as rota_administrador
from api.database import Base, engine
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Projeto de Transcrição")

app.include_router(rota_administrador, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
