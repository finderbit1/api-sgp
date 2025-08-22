from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from base import get_session
from .schema import FichaPedido, FichaPedidoCreate, FichaPedidoUpdate
import json
from datetime import datetime

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.post("/", response_model=FichaPedido)
def criar_pedido(ficha: FichaPedidoCreate, session: Session = Depends(get_session)):
    # Converter items para JSON string
    ficha_data = ficha.model_dump()
    if ficha_data.get('items'):
        ficha_data['items'] = json.dumps([item.model_dump() for item in ficha_data['items']])
    
    # Adicionar timestamps como string
    ficha_data['data_criacao'] = datetime.now().isoformat()
    ficha_data['ultima_atualizacao'] = datetime.now().isoformat()
    
    db_pedido = FichaPedido(**ficha_data)
    session.add(db_pedido)
    session.commit()
    session.refresh(db_pedido)
    return db_pedido

@router.get("/", response_model=list[FichaPedido])
def listar_pedidos(session: Session = Depends(get_session)):
    pedidos = session.exec(select(FichaPedido)).all()
    return pedidos

@router.get("/{pedido_id}", response_model=FichaPedido)
def obter_pedido(pedido_id: int, session: Session = Depends(get_session)):
    pedido = session.get(FichaPedido, pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido

@router.patch("/{pedido_id}", response_model=FichaPedido)
def atualizar_pedido(pedido_id: int, pedido_update: FichaPedidoUpdate, session: Session = Depends(get_session)):
    db_pedido = session.get(FichaPedido, pedido_id)
    if not db_pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    
    pedido_data = pedido_update.model_dump(exclude_unset=True)
    
    # Converter items para JSON string se existirem
    if 'items' in pedido_data and pedido_data['items'] is not None:
        pedido_data['items'] = json.dumps([item.model_dump() for item in pedido_data['items']])
    
    # Atualizar timestamp como string
    pedido_data['ultima_atualizacao'] = datetime.now().isoformat()
    
    for field, value in pedido_data.items():
        setattr(db_pedido, field, value)
    
    session.add(db_pedido)
    session.commit()
    session.refresh(db_pedido)
    return db_pedido

@router.delete("/{pedido_id}")
def deletar_pedido(pedido_id: int, session: Session = Depends(get_session)):
    db_pedido = session.get(FichaPedido, pedido_id)
    if not db_pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    
    session.delete(db_pedido)
    session.commit()
    return {"message": "Pedido deletado com sucesso"}
