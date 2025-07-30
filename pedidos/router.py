from fastapi import APIRouter,Depends
from .schema import List,FichaPedido
from database.db_fake import pedidos_fake

router = APIRouter(prefix="/pedidos",tags=["Pedidos"])


@router.get("/", response_model=List[FichaPedido])
def listar_pedidos():
    return pedidos_fake

@router.post("/")
def criar_pedido(ficha:FichaPedido):
    ficha_dict = ficha.dict()
    print(ficha_dict)
    return ficha_dict
