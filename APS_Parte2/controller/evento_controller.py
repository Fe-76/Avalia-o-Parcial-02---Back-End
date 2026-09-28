from fastapi import APIRouter, HTTPException, status

from model.evento import Evento
from service import evento_service, inscricao_service

router = APIRouter(prefix="/eventos", tags=["Eventos"])


@router.post("", response_model=Evento, status_code=status.HTTP_201_CREATED)
def cadastrar(evento: Evento):
    return evento_service.criar(evento)


@router.get("", response_model=list[Evento])
def listar():
    return evento_service.listar()


@router.get("/{id}", response_model=Evento)
def consultar(id: int):
    evento = evento_service.buscar(id)

    if evento is None:
        raise HTTPException(status_code=404, detail="Evento não encontrado.")

    return evento


@router.put("/{id}", response_model=Evento)
def atualizar(id: int, dados: Evento):
    evento = evento_service.atualizar(id, dados)

    if evento is None:
        raise HTTPException(status_code=404, detail="Evento não encontrado.")

    return evento


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir(id: int):
    evento = evento_service.excluir(id)

    if evento is None:
        raise HTTPException(status_code=404, detail="Evento não encontrado.")


@router.post(
    "/{evento_id}/inscricoes/{participante_id}",
    status_code=status.HTTP_201_CREATED
)
def inscrever(evento_id: int, participante_id: int):
    return inscricao_service.inscrever(evento_id, participante_id)


@router.get("/{evento_id}/inscricoes")
def inscritos(evento_id: int):
    return inscricao_service.listar_inscritos(evento_id)
