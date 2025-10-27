from typing import Optional

from sqlmodel import Field, SQLModel


class VendedorBase(SQLModel):
    nome: str
    email: Optional[str] = None
    telefone: Optional[str] = None
    comissao_percentual: float = Field(default=0)
    ativo: bool = Field(default=True)
    observacao: Optional[str] = None


class Vendedor(VendedorBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)


class VendedorCreate(VendedorBase):
    pass


class VendedorUpdate(SQLModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    comissao_percentual: Optional[float] = None
    ativo: Optional[bool] = None
    observacao: Optional[str] = None
