from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router  # Importa o router com as rotas definidas

app = FastAPI()

# Configuração de CORS para permitir chamadas do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Permite a origem do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir as rotas da API
app.include_router(router)