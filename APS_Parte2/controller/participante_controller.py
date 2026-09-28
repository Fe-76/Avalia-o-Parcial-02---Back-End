from fastapi import APIRouter, HTTPException, status

from model.participante import Participante
from service import participante_service

router = APIRouter(prefix="/participantes", tags=["Participantes"])


@router.post("", response_model=Participante, status_code=status.HTTP_201_CREATED)
def cadastrar(participante: Participante):
    return participante_service.criar(participante)


@router.get("", response_model=list[Participante])
def listar():
    return participante_service.listar()


@router.get("/{id}", response_model=Participante)
def consultar(id: int):
    participante = participante_service.buscar(id)

    if participante is None:
        raise HTTPException(status_code=404, detail="Participante não encontrado.")

    return participante


@router.put("/{id}", response_model=Participante)
def atualizar(id: int, dados: Participante):
    participante = participante_service.atualizar(id, dados)

    if participante is None:
        raise HTTPException(status_code=404, detail="Participante não encontrado.")

    return participante


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir(id: int):
    participante = participante_service.excluir(id)

    if participante is None:
        raise HTTPException(status_code=404, detail="Participante não encontrado.")
