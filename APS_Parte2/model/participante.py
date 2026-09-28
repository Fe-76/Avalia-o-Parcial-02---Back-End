from pydantic import BaseModel, EmailStr, Field


class Participante(BaseModel):
    id: int | None = None
    nome: str = Field(min_length=1)
    email: EmailStr
    curso: str
