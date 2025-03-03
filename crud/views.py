from sqlalchemy.orm import Session
from models.models import Leyendas, Categorias, Provincias, Canton, Distrito
from db.database import get_db
from fastapi import Depends, HTTPException
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import SQLAlchemyError


def view_leyendas(db: Session = Depends(get_db)):
    try:
        data = db.query(Leyendas).options(
            joinedload(Leyendas.categoria),
            joinedload(Leyendas.provincia),
            joinedload(Leyendas.canton),
            joinedload(Leyendas.distrito)
        ).all()
        return data
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener las leyendas: {str(e)}")


def view_leyenda_by_id(id: int, db: Session = Depends(get_db)):
    try:
        data = db.query(Leyendas).options(
            joinedload(Leyendas.categoria),
            joinedload(Leyendas.provincia),
            joinedload(Leyendas.canton),
            joinedload(Leyendas.distrito)
        ).filter(Leyendas.id == id).first()

        if not data:
            raise HTTPException(status_code=404, detail="Leyenda no encontrada")

        return data
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener la leyenda: {str(e)}")


def create_location(model, leyenda, db: Session = Depends(get_db)):
    try:
        instance = db.query(model).filter(model.nombre == leyenda).first()
        if not instance:
            instance = model(nombre=leyenda)
            db.add(instance)
        return instance
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error al crear la ubicación: {str(e)}")


def create_leyenda(leyenda, db: Session = Depends(get_db)):
    try:
        categoria = create_location(Categorias, leyenda.categoria.nombre, db)
        canton = create_location(Canton, leyenda.canton.nombre, db)
        provincia = create_location(Provincias, leyenda.provincia.nombre, db)
        distrito = create_location(Distrito, leyenda.distrito.nombre, db)

        db_leyenda = Leyendas(
            nombre=leyenda.nombre,
            txt_descrip=leyenda.txt_descrip,
            fecha_leyenda=leyenda.fecha_leyenda,
            historia=leyenda.historia,
            imagen=leyenda.imagen,
            id_categoria=categoria.id,
            id_provincia=provincia.id,
            id_canton=canton.id,
            id_distrito=distrito.id
        )

        db.add(db_leyenda)
        db.commit()
        db.refresh(db_leyenda)

        return {"message": "Leyenda creada exitosamente"}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear la leyenda: {str(e)}")


def update_leyenda(id: int, leyenda, db: Session = Depends(get_db)):
    try:
        data = db.query(Leyendas).filter(Leyendas.id == id).first()
        if not data:
            raise HTTPException(status_code=404, detail="Leyenda no encontrada")

        db.query(Leyendas).filter(Leyendas.id == id).update({
            Leyendas.nombre: leyenda.nombre,
            Leyendas.txt_descrip: leyenda.txt_descrip,
            Leyendas.fecha_leyenda: leyenda.fecha_leyenda,
            Leyendas.historia: leyenda.historia,
            Leyendas.imagen: leyenda.imagen,
            Leyendas.id_categoria: leyenda.id_categoria,
            Leyendas.id_provincia: leyenda.id_provincia,
            Leyendas.id_canton: leyenda.id_canton,
            Leyendas.id_distrito: leyenda.id_distrito
        })

        db.commit()
        return {"message": "Leyenda actualizada exitosamente"}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al actualizar la leyenda: {str(e)}")


def delete_leyenda(id: int, db: Session = Depends(get_db)):
    try:
        data = db.query(Leyendas).filter(Leyendas.id == id).first()
        if not data:
            raise HTTPException(status_code=404, detail="Leyenda no encontrada")

        db.delete(data)
        db.commit()

        return {"message": "Leyenda eliminada exitosamente"}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al eliminar la leyenda: {str(e)}")
