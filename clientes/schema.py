from pydantic import BaseModel

class Cliente(BaseModel):
    id: int
    nome: str
    cep: str
    cidade: str
    estado: str
    telefone: str
    

# Cliente(
#     id=0,
#     nome="Mateus",
#     cep="29701340",
#     cidade="colatina",
#     estado="es",
#     telefone="27 995900071"
# ),