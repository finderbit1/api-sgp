from typing import Optional

from sqlmodel import Field, SQLModel


class MaterialBase(SQLModel):
    nome: str
    tipo: str
    valor_metro: float = 0.0
    estoque_metros: float = 0.0
    ativo: bool = True
    observacao: Optional[str] = None


class Material(MaterialBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)


class MaterialCreate(MaterialBase):
    pass


class MaterialUpdate(SQLModel):
    nome: Optional[str] = None
    tipo: Optional[str] = None
    valor_metro: Optional[float] = None
    estoque_metros: Optional[float] = None
    ativo: Optional[bool] = None
    observacao: Optional[str] = None

