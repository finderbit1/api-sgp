from fastapi import FastAPI
from contextlib import asynccontextmanager

from fastapi.middleware.cors import CORSMiddleware
from base import engine,init_db


# Routers
from pedidos.router import router as pedidos_router
from clientes.router import router as clientes_router
from pagamentos.router import router as pagamentos_router
from envios.router import router as envios_router






@asynccontextmanager
async def lifespan(app: FastAPI):
    yield init_db()

app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, use o IP/URL específico
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(pedidos_router)
app.include_router(clientes_router)
app.include_router(pagamentos_router)
app.include_router(envios_router)

# @app.on_event("startup")
# def on_startup():
    


