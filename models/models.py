from sqlmodel import SQLModel, Field, Relationship
from typing import  List
from datetime import date

# Modelo de Categorías
class Categorias(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str

    leyendas: List["Leyendas"] = Relationship(back_populates="categoria")

# Modelo de Provincias
class Provincias(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str

    leyendas: List["Leyendas"] = Relationship(back_populates="provincia")

# Modelo de Canton
class Canton(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str

    leyendas: List["Leyendas"] = Relationship(back_populates="canton")

# Modelo de Distrito
class Distrito(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str

    leyendas: List["Leyendas"] = Relationship(back_populates="distrito")

# Modelo de Leyendas
class Leyendas(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str
    id_categoria: int = Field(default=None, foreign_key="categorias.id")
    txt_descrip: str
    fecha_leyenda: date 
    id_provincia: int = Field(default=None, foreign_key="provincias.id")
    id_canton: int = Field(default=None, foreign_key="canton.id")
    id_distrito: int = Field(default=None, foreign_key="distrito.id")
    historia: str 
    imagen: str 

    # Relaciones
    categoria: Categorias = Relationship(back_populates="leyendas")
    provincia: Provincias = Relationship(back_populates="leyendas")
    canton: Canton = Relationship(back_populates="leyendas")
    distrito: Distrito = Relationship(back_populates="leyendas")
