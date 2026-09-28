# API de Eventos Acadêmicos

Projeto da APS de Back-End feito com Python e FastAPI.

Nesta versão estão implementados os eventos, participantes e inscrições.

## Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
uvicorn main:app --reload
```

Swagger:

`http://127.0.0.1:8000/docs`

## Organização

```text
main.py
controller/
model/
service/
```

O controller cuida das rotas, o model dos dados e o service das operações e regras do sistema.

Os dados ficam em memória e são perdidos quando a aplicação é reiniciada.

## Eventos

- POST `/eventos`
- GET `/eventos`
- GET `/eventos/{id}`
- PUT `/eventos/{id}`
- DELETE `/eventos/{id}`

## Participantes

- POST `/participantes`
- GET `/participantes`
- GET `/participantes/{id}`
- PUT `/participantes/{id}`
- DELETE `/participantes/{id}`

## Inscrições

- POST `/eventos/{evento_id}/inscricoes/{participante_id}`
- GET `/eventos/{evento_id}/inscricoes`

Na inscrição são verificadas as seguintes situações:

- evento não existe;
- participante não existe;
- participante já está inscrito;
- evento não possui mais vagas.

## Exemplo de evento

```json
{
  "titulo": "Palestra sobre APIs",
  "descricao": "Palestra sobre desenvolvimento Back-End",
  "data": "2026-10-20",
  "horario": "19:30",
  "local": "Auditório",
  "capacidade": 50,
  "categoria": "Palestra"
}
```

## Exemplo de participante

```json
{
  "nome": "João da Silva",
  "email": "joao@email.com",
  "curso": "Engenharia de Software"
}
```

## Exemplo de inscrição

Depois de cadastrar um evento com ID `1` e um participante com ID `1`:

```text
POST /eventos/1/inscricoes/1
```

Resposta:

```json
{
  "mensagem": "Inscrição realizada com sucesso.",
  "evento_id": 1,
  "participante_id": 1
}
```

## Erros

Se o evento não existir:

```json
{
  "detail": "Evento não encontrado."
}
```

Se o participante já estiver inscrito:

```json
{
  "detail": "Participante já está inscrito neste evento."
}
```

Se não houver vagas:

```json
{
  "detail": "Não existem vagas disponíveis para este evento."
}
```

O FastAPI também retorna `422` quando os dados enviados não passam pelas validações do Pydantic, como um e-mail inválido ou uma capacidade igual a zero.

## Testes no Swagger

Uma sequência simples para demonstrar o projeto é:

1. Cadastrar um evento;
2. Cadastrar um participante;
3. Consultar os dois;
4. Atualizar um deles;
5. Fazer a inscrição;
6. Consultar os inscritos;
7. Tentar fazer a mesma inscrição novamente;
8. Testar um ID que não existe;
9. Excluir um registro.
