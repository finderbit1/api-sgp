from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from base import create_db_and_tables
from config import settings

# Routers
from pedidos.router import router as pedidos_router
from clientes.router import router as clientes_router
from pagamentos.router import router as pagamentos_router
from envios.router import router as envios_router
from admin.router import router as admin_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield create_db_and_tables()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    lifespan=lifespan
)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão dos routers
app.include_router(pedidos_router, prefix=settings.API_V1_STR)
app.include_router(clientes_router, prefix=settings.API_V1_STR)
app.include_router(pagamentos_router, prefix=settings.API_V1_STR)
app.include_router(envios_router, prefix=settings.API_V1_STR)
app.include_router(admin_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {
        "message": "API Sistema de Fichas",
        "version": settings.VERSION,
        "docs": "/docs"
    }
    
    


