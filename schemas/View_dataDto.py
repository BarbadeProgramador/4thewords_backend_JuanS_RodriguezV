from pydantic import BaseModel
from datetime import date




class CategoriaDTO(BaseModel):
    nombre: str

class ProvinciaDTO(BaseModel):
    nombre: str

class CantonDTO(BaseModel):
    nombre: str

class DistritoDTO(BaseModel):
    nombre: str

class LeyendaDto(BaseModel):
    id: int
    nombre: str
    # id_categoria: int
    txt_descrip: str
    fecha_leyenda: date
    # id_provincia: int
    # id_canton: int
    # id_distrito: int
    historia: str
    imagen: str

    categoria: CategoriaDTO  # Relación
    provincia: ProvinciaDTO
    canton: CantonDTO
    distrito: DistritoDTO