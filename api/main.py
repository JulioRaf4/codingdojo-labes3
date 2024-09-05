from api.administradores.routes import route as rota_administrador
from api.locais.routes import route as rota_locais
from api.database import Base, engine
from api.locais.database import Base1, engine1
from fastapi import FastAPI
import uvicorn


Base.metadata.create_all(bind=engine)
Base1.metadata.create_all(bind=engine1)

app = FastAPI(title='Coding Dojo')

# Adicione as novas rotas aqui
# app.include_router(rota_exemplo, prefix="/api")
app.include_router(rota_administrador, prefix='/api')
app.include_router(rota_locais, prefix='/api')

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
