from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
from schemas.item import Item

class Prioridade(Enum):
    NORMAL = 0
    MEDIA = 1
    ALTA = 2

class FichaPedido(BaseModel):
    numero: str
    cliente: str
    telefone: Optional[str]
    cidade: Optional[str]
    data_entrada: str
    data_entrega: str
    status: str  # 'pendente' ou 'pronto'
    prioridade: Prioridade
    financeiro: bool = False
    sublimação: bool = False
    costura: bool = False
    expedicao: bool = False
    observacao: Optional[str] = ""
    tipo_pagamento: Optional[str]
    obs_pagamento: Optional[str]
    valor_total: Optional[str]
    valor_frete: Optional[str]
    items: List[Item] = []
