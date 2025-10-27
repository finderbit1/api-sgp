from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from base import get_session
from .schema import Material, MaterialCreate, MaterialUpdate

router = APIRouter(prefix="/materiais", tags=["Materiais"])


@router.get("/", response_model=list[Material])
def list_materiais(session: Session = Depends(get_session)):
    materiais = session.exec(select(Material)).all()
    return materiais


@router.get("/{material_id}", response_model=Material)
def get_material(material_id: int, session: Session = Depends(get_session)):
    material = session.get(Material, material_id)
    if not material:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Material não encontrado")
    return material


@router.post("/", response_model=Material, status_code=status.HTTP_201_CREATED)
def create_material(material: MaterialCreate, session: Session = Depends(get_session)):
    db_material = Material(**material.model_dump())
    session.add(db_material)
    session.commit()
    session.refresh(db_material)
    return db_material


@router.patch("/{material_id}", response_model=Material)
def update_material(
    material_id: int,
    material_update: MaterialUpdate,
    session: Session = Depends(get_session),
):
    db_material = session.get(Material, material_id)
    if not db_material:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Material não encontrado")

    update_data = material_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_material, field, value)

    session.add(db_material)
    session.commit()
    session.refresh(db_material)
    return db_material


@router.delete("/{material_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_material(material_id: int, session: Session = Depends(get_session)):
    db_material = session.get(Material, material_id)
    if not db_material:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Material não encontrado")

    session.delete(db_material)
    session.commit()
    return None

