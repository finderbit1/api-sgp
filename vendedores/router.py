from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from base import get_session
from .schema import Vendedor, VendedorCreate, VendedorUpdate

router = APIRouter(prefix="/vendedores", tags=["Vendedores"])


@router.get("/", response_model=list[Vendedor])
def list_vendedores(session: Session = Depends(get_session)):
    vendedores = session.exec(select(Vendedor)).all()
    return vendedores


@router.get("/ativos", response_model=list[Vendedor])
def list_vendedores_ativos(session: Session = Depends(get_session)):
    statement = select(Vendedor).where(Vendedor.ativo.is_(True))
    vendedores = session.exec(statement).all()
    return vendedores


@router.get("/{vendedor_id}", response_model=Vendedor)
def get_vendedor(vendedor_id: int, session: Session = Depends(get_session)):
    vendedor = session.get(Vendedor, vendedor_id)
    if not vendedor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendedor não encontrado")
    return vendedor


@router.post("/", response_model=Vendedor, status_code=status.HTTP_201_CREATED)
def create_vendedor(vendedor: VendedorCreate, session: Session = Depends(get_session)):
    db_vendedor = Vendedor(**vendedor.model_dump())
    session.add(db_vendedor)
    session.commit()
    session.refresh(db_vendedor)
    return db_vendedor


@router.patch("/{vendedor_id}", response_model=Vendedor)
def update_vendedor(
    vendedor_id: int,
    vendedor_update: VendedorUpdate,
    session: Session = Depends(get_session),
):
    db_vendedor = session.get(Vendedor, vendedor_id)
    if not db_vendedor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendedor não encontrado")

    update_data = vendedor_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_vendedor, field, value)

    session.add(db_vendedor)
    session.commit()
    session.refresh(db_vendedor)
    return db_vendedor


@router.delete("/{vendedor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendedor(vendedor_id: int, session: Session = Depends(get_session)):
    db_vendedor = session.get(Vendedor, vendedor_id)
    if not db_vendedor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendedor não encontrado")

    session.delete(db_vendedor)
    session.commit()
    return None
