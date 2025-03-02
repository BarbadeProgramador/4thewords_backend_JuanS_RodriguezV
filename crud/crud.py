from sqlalchemy.orm import Session
from models.models import Leyendas
from db.database import get_db
from fastapi import Depends
from sqlalchemy.orm import selectinload, join,joinedload


def view_leyendas(db: Session = Depends(get_db)):

    data = (db.query(Leyendas).options(    
            joinedload(Leyendas.categoria),
            joinedload(Leyendas.provincia),
            joinedload(Leyendas.canton),
            joinedload(Leyendas.distrito)).all()) 
  
    # print(data)

    return data

def view_leyenda_by_id(id: int, db: Session = Depends(get_db)):

    data = (db.query(Leyendas).options(
        joinedload(Leyendas.categoria),
        joinedload(Leyendas.provincia),
        joinedload(Leyendas.canton),
        joinedload(Leyendas.distrito)).filter(Leyendas.id == id).first())
    
    val = 1
    return data