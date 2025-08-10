from fastapi import APIRouter,Depends
from database.db_fake import Transportadoras
from .schema import Envio,List
from .crud import search_id

router = APIRouter(prefix="/tipos-envios",tags=["Tipos de Envios"])

@router.get("/", response_model=List[Envio])
def listar_formas_envios():
    return Transportadoras


@router.get("/{id}",response_model=Envio)
def buscar_envio(id):
    return search_id(id)