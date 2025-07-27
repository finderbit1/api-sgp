from typing import List,Optional
from pydantic import BaseModel
from datetime import date
from enum import Enum



class Prioridade(Enum):
    NORMAL = 0
    MEDIA = 1
    ALTA = 2


class Pedido(BaseModel):
    numero: str
    cliente: str
    data: str  # Pode ser str no formato 'YYYY-MM-DD'
    status: str  # 'pendente' ou 'pronto'
    prioridade: bool
    financeiro: bool
    sublimação: bool
    costura: bool
    expedicao: bool
    # items: List[Item]



