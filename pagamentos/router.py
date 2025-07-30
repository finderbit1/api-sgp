from fastapi import APIRouter,Depends
from .schema import Payments,List
from database.db_fake import tiposPagamentos

router = APIRouter(prefix="/tipos-pagamentos",tags=["Pagamentos"])

# Tipos de Pagamento
@router.get("/", response_model=List[Payments])
def listar_pedidos():
    return tiposPagamentos
