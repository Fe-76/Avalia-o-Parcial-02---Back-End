from datetime import date
from pydantic import BaseModel, Field


class Evento(BaseModel):
    id: int | None = None
    titulo: str = Field(min_length=1)
    descricao: str
    data: date
    horario: str
    local: str
    capacidade: int = Field(gt=0)
    categoria: str
