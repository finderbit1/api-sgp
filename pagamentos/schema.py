from typing import Optional

from sqlmodel import Field, SQLModel


class PaymentsBase(SQLModel):
    nome: str
    parcelas_max: int = 1
    taxa_percentual: float = 0
    ativo: bool = True
    observacao: Optional[str] = None


class Payments(PaymentsBase, table=True):
    __tablename__ = "payment"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)


class PaymentsCreate(PaymentsBase):
    pass


class PaymentsUpdate(SQLModel):
    nome: Optional[str] = None
    parcelas_max: Optional[int] = None
    taxa_percentual: Optional[float] = None
    ativo: Optional[bool] = None
    observacao: Optional[str] = None
    
