from pydantic import BaseModel


class Cliente(BaseModel):
    id: int
    nome: str
    cep:str
    cidade:str
    estado:str
    telefone:str

