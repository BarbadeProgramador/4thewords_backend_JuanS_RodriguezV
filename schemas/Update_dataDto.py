from pydantic import BaseModel
from datetime import date
from typing import Optional
from schemas.View_dataDto import CategoriaDTO, ProvinciaDTO, CantonDTO, DistritoDTO





class LeyendaDto_Update(BaseModel):
    id: int
    nombre: Optional[str] = None
    txt_descrip: Optional[str] = None
    fecha_leyenda: Optional[date] = None
    historia: Optional[str] = None
    imagen: Optional[str] = None
    id_categoria: Optional[int] = None
    id_provincia: Optional[int] = None
    id_canton: Optional[int] = None
    id_distrito: Optional[int] = None
    
    # categoria: Optional[CategoriaDTO] = None  # Relación
    # provincia: Optional[ProvinciaDTO] = None
    # canton: Optional[CantonDTO] = None
    # distrito: Optional[DistritoDTO] = None