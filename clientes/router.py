from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from base import get_session
from models import Cliente

router = APIRouter(prefix='/clientes',tags=["Clientes"])

@router.post("/", response_model=Cliente)
def create_cliente(cliente: Cliente, session: Session = Depends(get_session)):
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    return cliente

@router.get("/", response_model=list[Cliente])
def read_clientes(session: Session = Depends(get_session)):
    clientes = session.exec(select(Cliente)).all()
    return clientes
