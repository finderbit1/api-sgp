from typing import Optional

from sqlmodel import Field, SQLModel


class DesignerBase(SQLModel):
    nome: str
    email: Optional[str] = None
    telefone: Optional[str] = None
    ativo: bool = True
    observacao: Optional[str] = None


class Designer(DesignerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)


class DesignerCreate(DesignerBase):
    pass


class DesignerUpdate(SQLModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    ativo: Optional[bool] = None
    observacao: Optional[str] = None

