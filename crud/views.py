from sqlalchemy.orm import Session
from models.models import Leyendas , Categorias , Provincias , Canton , Distrito
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
    
    return data

def create_leyenda(leyenda ,db: Session = Depends(get_db)):

    # data = leyenda.dict()
    categoria = db.query(Categorias).filter(Categorias.nombre == leyenda.categoria.nombre).first()
    if not categoria:
        categoria = Categorias(
            nombre=leyenda.categoria.nombre
        )
        db.add(categoria)
        db.commit()
        db.refresh(categoria)

    canton = db.query(Canton).filter(Canton.nombre == leyenda.canton.nombre).first()
    if not canton:
        canton = Canton(
            nombre=leyenda.canton.nombre
        )
        db.add(canton)
        db.commit()
        db.refresh(canton)

    provincia = db.query(Provincias).filter(Provincias.nombre == leyenda.provincia.nombre).first()
    if not provincia:
        provincia = Provincias(
            nombre=leyenda.provincia.nombre
        )
        db.add(provincia)
        db.commit()
        db.refresh(provincia)
    
    distrito = db.query(Distrito).filter(Distrito.nombre == leyenda.distrito.nombre).first()
    if not distrito:
        distrito = Distrito(
            nombre=leyenda.distrito.nombre
        )
        db.add(distrito)
        db.commit()
        db.refresh(distrito)
   

    db_leyenda = Leyendas(
        nombre = leyenda.nombre,
        txt_descrip = leyenda.txt_descrip,
        fecha_leyenda = leyenda.fecha_leyenda,
        historia = leyenda.historia,
        imagen = leyenda.imagen,
        id_categoria = categoria.id,
        id_provincia = provincia.id,
        id_canton = canton.id,
        id_distrito = distrito.id
    )

    db.add(db_leyenda)
    
    db.commit()

    db.refresh(db_leyenda)


    print(db_leyenda)

    return {"message": "Leyenda creada exitosamente"}

    
