from datetime import date
from typing import List
from schemas.ficha import Ficha
from schemas.pedido import Pedido
from schemas.cliente import Cliente


# Simulando um banco de dados em memória
pedidos_fake: List[Pedido] = [
    Pedido(
        numero="001",
        cliente="Mateus José da Silva",
        data=str(date.today().strftime("%d/%m/%Y")),
        status="pendente",
        prioridade=True,
        financeiro=False,
        sublimação=False,
        costura=False,
        expedicao=False
    ),
    Pedido(
        numero="002",
        cliente="Carlos Souza",
        data=str(date.today().strftime("%d/%m/%Y")),
        status="pronto",
        prioridade=False,
        financeiro=True,
        sublimação=True,
        costura=True,
        expedicao=True
    )
]

clientes: List[Cliente]= [
    Cliente(
        id=0,
        nome="Mateus",
        cep="29701340",
        cidade="colatina",
        estado="es",
        telefone="27 995900071"
    ),
        Cliente(
        id=1,
        nome="Breno Polezi",
        cep="29701340",
        cidade="linhares",
        estado="es",
        telefone="27 000900071"
    ),
]




