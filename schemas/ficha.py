from typing import List
from pydantic import BaseModel
from .item import Item

class Ficha(BaseModel):
    numeroPedido: str
    nomeCliente: str
    telefoneCliente: str
    dataEntrada: str
    dataEntrega: str
    cidadeCliente: str
    observacao: str
    prioridade: str
    items: List[Item]
    valorTotal: str
    valorFrete: str
    tipoPagamento: str
    obsPagamento: str

