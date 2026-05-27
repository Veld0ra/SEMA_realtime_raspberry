import asyncio

from core.connection import conectar
from core.sender import (
    iniciar_sessao,
    enviar_texto,
    criar_resposta
)
from core.receiver import receber_resposta


async def main():

    print("Tentando conectar...")

    ws = await conectar()

    print("🟢 Conectado no Realtime!" )

    # inicia sessão
    await iniciar_sessao(ws)

    while True:

        texto = input("\nVocê: ")

        if texto.lower() == "sair":
            break

        # envia mensagem
        await enviar_texto(ws, texto)

        # pede resposta
        await criar_resposta(ws)

        # recebe resposta
        await receber_resposta(ws)

    await ws.close()


asyncio.run(main())


