from sqlmodel import SQLModel, Field
from typing import List, Optional
from enum import Enum
from producoes import ItemProducao

class Prioridade(Enum):
    NORMAL = "NORMAL"
    ALTA = "ALTA"

class FichaPedido(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    numero: str
    cliente: str
    telefone_cliente: Optional[str] = None
    cidade_cliente: Optional[str] = None
    data_entrada: str
    data_entrega: str
    status: str  # 'pendente' ou 'pronto'
    prioridade: str  # 'NORMAL' ou 'ALTA'
    financeiro: bool = False
    sublimação: bool = False
    costura: bool = False
    expedicao: bool = False
    observacao: Optional[str] = ""
    tipo_pagamento: Optional[str] = None
    obs_pagamento: Optional[str] = None
    valor_total: Optional[str] = None
    valor_frete: Optional[str] = None
    valor_itens: Optional[str] = None
    forma_envio: Optional[str] = None
    forma_envio_id: Optional[int] = None
    data_criacao: Optional[str] = None
    ultima_atualizacao: Optional[str] = None
    items: Optional[str] = None  # JSON string para os items

class FichaPedidoBase(SQLModel):
    numero: str
    cliente: str
    telefone_cliente: Optional[str] = None
    cidade_cliente: Optional[str] = None
    data_entrada: str
    data_entrega: str
    status: str  # 'pendente' ou 'pronto'
    prioridade: Prioridade
    financeiro: bool = False
    sublimação: bool = False
    costura: bool = False
    expedicao: bool = False
    observacao: Optional[str] = ""
    tipo_pagamento: Optional[str] = None
    obs_pagamento: Optional[str] = None
    valor_total: Optional[str] = None
    valor_frete: Optional[str] = None
    valor_itens: Optional[str] = None
    forma_envio: Optional[str] = None
    forma_envio_id: Optional[int] = None
    data_criacao: Optional[str] = None
    ultima_atualizacao: Optional[str] = None

class FichaPedidoCreate(FichaPedidoBase):
    items: Optional[List[ItemProducao]] = []

class FichaPedidoUpdate(SQLModel):
    numero: Optional[str] = None
    cliente: Optional[str] = None
    telefone_cliente: Optional[str] = None
    cidade_cliente: Optional[str] = None
    data_entrada: Optional[str] = None
    data_entrega: Optional[str] = None
    status: Optional[str] = None
    prioridade: Optional[Prioridade] = None
    financeiro: Optional[bool] = None
    sublimação: Optional[bool] = None
    costura: Optional[bool] = None
    expedicao: Optional[bool] = None
    observacao: Optional[str] = None
    tipo_pagamento: Optional[str] = None
    obs_pagamento: Optional[str] = None
    valor_total: Optional[str] = None
    valor_frete: Optional[str] = None
    valor_itens: Optional[str] = None
    forma_envio: Optional[str] = None
    forma_envio_id: Optional[int] = None
    data_criacao: Optional[str] = None
    ultima_atualizacao: Optional[str] = None
    items: Optional[List[ItemProducao]] = None



