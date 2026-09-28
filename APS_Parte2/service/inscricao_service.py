from fastapi import HTTPException

from service.evento_service import buscar as buscar_evento
from service.participante_service import buscar as buscar_participante

inscricoes = []


def inscrever(evento_id: int, participante_id: int):
    evento = buscar_evento(evento_id)

    if evento is None:
        raise HTTPException(status_code=404, detail="Evento não encontrado.")

    participante = buscar_participante(participante_id)

    if participante is None:
        raise HTTPException(status_code=404, detail="Participante não encontrado.")

    for inscricao in inscricoes:
        if (
            inscricao["evento_id"] == evento_id
            and inscricao["participante_id"] == participante_id
        ):
            raise HTTPException(
                status_code=400,
                detail="Participante já está inscrito neste evento."
            )

    quantidade = 0

    for inscricao in inscricoes:
        if inscricao["evento_id"] == evento_id:
            quantidade += 1

    if quantidade >= evento.capacidade:
        raise HTTPException(
            status_code=400,
            detail="Não existem vagas disponíveis para este evento."
        )

    inscricoes.append({
        "evento_id": evento_id,
        "participante_id": participante_id
    })

    return {
        "mensagem": "Inscrição realizada com sucesso.",
        "evento_id": evento_id,
        "participante_id": participante_id
    }


def listar_inscritos(evento_id: int):
    evento = buscar_evento(evento_id)

    if evento is None:
        raise HTTPException(status_code=404, detail="Evento não encontrado.")

    lista = []

    for inscricao in inscricoes:
        if inscricao["evento_id"] == evento_id:
            participante = buscar_participante(inscricao["participante_id"])

            if participante:
                lista.append(participante)

    return lista
