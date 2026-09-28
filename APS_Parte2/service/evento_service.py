from model.evento import Evento

eventos = []
ultimo_id = 0


def criar(evento: Evento):
    global ultimo_id

    ultimo_id += 1
    evento.id = ultimo_id
    eventos.append(evento)

    return evento


def listar():
    return eventos


def buscar(id: int):
    for evento in eventos:
        if evento.id == id:
            return evento

    return None


def atualizar(id: int, dados: Evento):
    for i, evento in enumerate(eventos):
        if evento.id == id:
            dados.id = id
            eventos[i] = dados
            return dados

    return None


def excluir(id: int):
    for i, evento in enumerate(eventos):
        if evento.id == id:
            return eventos.pop(i)

    return None
