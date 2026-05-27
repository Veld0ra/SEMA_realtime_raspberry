import json


async def iniciar_sessao(ws, memoria_fixa="", memoria_buffer=""):

    instructions = f"""
Você é a SEMA, uma assistente útil, amigavel e legal.

# MEMÓRIA PERSISTENTE
{memoria_fixa}

# CONTEXTO RECENTE
{memoria_buffer}

Regras:
- Responda de forma clara
- Use o contexto quando necessário
"""

    await ws.send(json.dumps({
        "type": "session.update",
        "session": {
            "type": "realtime",
            "instructions": instructions
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
