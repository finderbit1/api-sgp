from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from base import get_session
from .schema import Designer, DesignerCreate, DesignerUpdate

router = APIRouter(prefix="/designers", tags=["Designers"])


@router.get("/", response_model=list[Designer])
def list_designers(session: Session = Depends(get_session)):
    designers = session.exec(select(Designer)).all()
    return designers


@router.get("/{designer_id}", response_model=Designer)
def get_designer(designer_id: int, session: Session = Depends(get_session)):
    designer = session.get(Designer, designer_id)
    if not designer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Designer não encontrado")
    return designer


@router.post("/", response_model=Designer, status_code=status.HTTP_201_CREATED)
def create_designer(designer: DesignerCreate, session: Session = Depends(get_session)):
    db_designer = Designer(**designer.model_dump())
    session.add(db_designer)
    session.commit()
    session.refresh(db_designer)
    return db_designer


@router.patch("/{designer_id}", response_model=Designer)
def update_designer(
    designer_id: int,
    designer_update: DesignerUpdate,
    session: Session = Depends(get_session),
):
    db_designer = session.get(Designer, designer_id)
    if not db_designer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Designer não encontrado")

    update_data = designer_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_designer, field, value)

    session.add(db_designer)
    session.commit()
    session.refresh(db_designer)
    return db_designer


@router.delete("/{designer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_designer(designer_id: int, session: Session = Depends(get_session)):
    db_designer = session.get(Designer, designer_id)
    if not db_designer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Designer não encontrado")

    session.delete(db_designer)
    session.commit()
    return None

