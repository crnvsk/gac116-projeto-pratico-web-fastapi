from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router  # Importa o router com as rotas definidas

app = FastAPI()

# Configuração de CORS para permitir chamadas do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (somente para testar)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluindo as rotas
app.include_router(router)
