from model.participante import Participante

participantes = []
ultimo_id = 0


def criar(participante: Participante):
    global ultimo_id

    ultimo_id += 1
    participante.id = ultimo_id
    participantes.append(participante)

    return participante


def listar():
    return participantes


def buscar(id: int):
    for participante in participantes:
        if participante.id == id:
            return participante

    return None


def atualizar(id: int, dados: Participante):
    for i, participante in enumerate(participantes):
        if participante.id == id:
            dados.id = id
            participantes[i] = dados
            return dados

    return None


def excluir(id: int):
    for i, participante in enumerate(participantes):
        if participante.id == id:
            return participantes.pop(i)

    return None
