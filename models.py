from typing import Optional
from sqlmodel import SQLModel, Field

class Cliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    cep: str
    cidade: str
    estado: str
    telefone: str


class Envio(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    value: Optional[float] = None


class Payment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(unique=True)


class Vendedor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Designer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
