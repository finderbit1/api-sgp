from fastapi import APIRouter,Depends
from .schema import Envio,List
from database.db_fake import Transportadoras

router = APIRouter(prefix="/tipos-envios",tags=["Tipos de Envios"])

@router.get("/", response_model=List[Envio])
def listar_formas_envios():
    return Transportadoras
