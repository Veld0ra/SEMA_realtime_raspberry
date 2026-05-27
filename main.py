import asyncio

from core.connection import conectar
from core.sender import (
    iniciar_sessao,
    enviar_texto,
    criar_resposta
)
from core.receiver import receber_resposta

from memory.memory import Memory


async def main():

    print("Tentando conectar...")

    ws = await conectar()

    print("🟢 Conectado no Realtime!")

    # -------------------------
    # MEMÓRIA
    # -------------------------
    memory = Memory()
    memory.iniciar_dia()

    memoria_fixa = memory.ler_memoria_fixa()

    buffer = memory.get_buffer()

    memoria_buffer = "\n".join([f"{r}: {t}" for r, t in buffer])

    # -------------------------
    # INICIA SESSÃO COM MEMÓRIA
    # -------------------------
    await iniciar_sessao(ws, memoria_fixa, memoria_buffer)

    while True:

        texto = input("\nVocê: ")

        if texto.lower() == "sair":
            break

        # salva memória
        memory.add_buffer("user", texto)
        memory.salvar_conversa("Usuário", texto)

        # envia mensagem
        await enviar_texto(ws, texto)

        # pede resposta
        await criar_resposta(ws)

        # recebe resposta
        resposta = await receber_resposta(ws)

        # salva resposta
        memory.add_buffer("sema", resposta)
        memory.salvar_conversa("SEMA", resposta)

    await ws.close()


asyncio.run(main())
