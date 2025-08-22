from sqlmodel import SQLModel, Field
from typing import Literal, Union, Optional


class AcabamentoModel(SQLModel):
    overloque: bool = False
    elastico: bool = False
    ilhos: bool = False


class PainelModel(SQLModel):
    id: Optional[int] = None
    tipo_producao: Literal["painel"]
    descricao: str
    largura: Optional[str] = ''
    altura: Optional[str] = ''
    metro_quadrado: Optional[str] = ''
    imagem: Optional[str] = None
    vendedor: Optional[str] = ''
    designer: Optional[str] = ''
    tecido: Optional[str] = ''
    acabamento: Optional[str] = ''
    emenda: Optional[str] = 'sem-emenda'
    observacao: Optional[str] = ''
    valor_unitario: Optional[str] = ''


class TotemModel(SQLModel):
    id: Optional[int] = None
    tipo_producao: Literal["totem"]
    descricao: str
    largura: Optional[str] = ""
    altura: Optional[str] = ""
    metro_quadrado: Optional[str] = ""
    vendedor: Optional[str] = ""
    designer: Optional[str] = ""
    tecido: Optional[str] = ""
    acabamento: Optional[str] = ""
    emenda: Optional[str] = ""
    observacao: Optional[str] = ""
    valor_unitario: Optional[str] = ""
    ilhos_qtd: Optional[int] = None
    ilhos_valor_unitario: Optional[str] = ""
    ilhos_distancia: Optional[str] = ""
    imagem: Optional[str] = None


class LonaModel(SQLModel):
    id: Optional[int] = None
    tipo_producao: Literal["lona"]
    descricao: str
    largura: Optional[str] = ""
    altura: Optional[str] = ""
    metro_quadrado: Optional[str] = ""
    vendedor: Optional[str] = ""
    designer: Optional[str] = ""
    tecido: Optional[str] = ""
    acabamento: Optional[str] = ""
    emenda: Optional[str] = ""
    observacao: Optional[str] = ""
    valor_unitario: Optional[str] = ""
    imagem: Optional[str] = None


# UNION DISCRIMINADA (baseada em tipo_producao)
ItemProducao = Union[PainelModel, TotemModel, LonaModel]