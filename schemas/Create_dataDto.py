from pydantic import BaseModel
from datetime import date
from schemas.View_dataDto import CategoriaDTO, ProvinciaDTO, CantonDTO, DistritoDTO



# class CategoriaDTO(BaseModel):
#     nombre: str

# class ProvinciaDTO(BaseModel):
#     nombre: str

# class CantonDTO(BaseModel):
#     nombre: str
 
# class DistritoDTO(BaseModel):
#     nombre: str

class LeyendaDto_Create(BaseModel):
    nombre: str
    txt_descrip: str
    fecha_leyenda: date
    historia: str
    imagen: str
    # id_categoria: int
    # id_provincia: int
    # id_canton: int
    # id_distrito: int

    categoria: CategoriaDTO  # Relación
    provincia: ProvinciaDTO
    canton: CantonDTO
    distrito: DistritoDTO