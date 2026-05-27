import json


async def iniciar_sessao(ws):

    await ws.send(json.dumps({
        "type": "session.update",
        "session": {
            "type": "realtime",
            "instructions": "Você é a SEMA, uma assistente útil e direta."
        }
    }))


async def enviar_texto(ws, texto):

    await ws.send(json.dumps({
        "type": "conversation.item.create",
        "item": {
            "type": "message",
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": texto
                }
            ]
        }
    }))


async def criar_resposta(ws):

    await ws.send(json.dumps({
        "type": "response.create"
    }))

