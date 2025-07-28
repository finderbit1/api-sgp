from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from schemas.ficha import Ficha
from schemas.pedido import FichaPedido
from schemas.cliente import Cliente
from schemas.payments import Payments
from schemas.envio import Envio
from database.db_fake import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, use o IP/URL específico
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/pedidos", response_model=List[FichaPedido])
def listar_pedidos():
    return pedidos_fake

@app.post("/pedidos")
def criar_pedido(ficha:Ficha):
    ficha_dict = ficha.dict()
    print(ficha_dict)
    return ficha_dict


# Tipos de Pagamento
@app.get("/tipos-pagamentos", response_model=List[Payments])
def listar_pedidos():
    return tiposPagamentos

# Formas de Envio
@app.get("/tipos-envios", response_model=List[Envio])
def listar_formas_envios():
    return Transportadoras



# Clientes
@app.get("/clientes",response_model=List[Cliente])
def listar_clientes():
    return clientes
