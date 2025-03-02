from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from models.models import Leyendas
from schemas.View_dataDto import LeyendaDto
from crud.crud import view_leyendas , view_leyenda_by_id


router = APIRouter(prefix="/leyendas", tags=["Leyendas"])

@router.get("/", response_model=list[LeyendaDto])
def view_all(db: Session = Depends(get_db)):
    data =  view_leyendas(db)
    return data

@router.get("/{id}", response_model=LeyendaDto)
def view_legend_id(id: int, db: Session = Depends(get_db)):
    data = view_leyenda_by_id(id, db)
    return data

@router.delete("/{id}", response_model=LeyendaDto)
def delete_legend_id(id: int, db: Session = Depends(get_db)):
    data = view_leyenda_by_id(id, db)
    db.delete(data)
    db.commit()
    return data
