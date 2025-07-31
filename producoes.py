from pydantic import BaseModel, Field
from typing import Literal, Union,Optional
from typing_extensions import Annotated


class AcabamentoModel(BaseModel):
    overloque: bool = False
    elastico: bool = False
    ilhos: bool = False


class PainelModel(BaseModel):
    tipoProducao: Literal["painel"]
    descricao: Optional[str] = ''
    largura: Optional[str] = ''
    altura: Optional[str] = ''
    imagem:str
    vendedor: Optional[str] = ''
    designer: Optional[str] = ''
    tecido: Optional[str] = ''
    acabamento: AcabamentoModel = AcabamentoModel()
    emenda: Optional[str] = 'sem-emenda'
    observacao: Optional[str] = ''
    valorPainel: Optional[str] = ''
    ilhosQtd: Optional[str] = ''
    ilhosValorUnitario: Optional[str] = ''
    ilhosDistancia: Optional[str] = ''


class TotemModel(BaseModel):
    tipoProducao: Literal["totem"]
    descricao: str
    altura: Optional[str] = ""
    material: Optional[str] = ""
    valor: Optional[str] = ""


class LonaModel(BaseModel):
    tipoProducao: Literal["lona"]
    descricao: str
    metragem: Optional[str] = ""
    gramatura: Optional[str] = ""


# UNION DISCRIMINADA (baseada em tipoProducao)
ItemProducao = Annotated[
    Union[PainelModel, TotemModel, LonaModel],
    Field(discriminator="tipoProducao")
]