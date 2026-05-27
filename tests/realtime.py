import asyncio
import websockets
import json
import os

API_KEY = os.getenv("OPENAI_API_KEY")

URL = "wss://api.openai.com/v1/realtime?model=gpt-realtime"


async def main():

    if not API_KEY:
        print("❌ OPENAI_API_KEY não encontrada")
        return

    print("Tentando conectar...")

    async with websockets.connect(
        URL,
        extra_headers={
            "Authorization": f"Bearer {API_KEY}"
        }
    ) as ws:

        print("🟢 Conectado no Realtime!")

        # sessão
        await ws.send(json.dumps({
            "type": "session.update",
            "session": {
                "type": "realtime",
                "instructions": "Você é a SEMA, uma assistente útil e direta."
            }
        }))

        while True:

            texto = input("\nVocê: ")

            if texto.lower() == "sair":
                break

            # envia mensagem
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

            # cria resposta
            await ws.send(json.dumps({
                "type": "response.create"
            }))

            print("SEMA: ", end="", flush=True)

            while True:

                raw = await ws.recv()

                event = json.loads(raw)

                event_type = event.get("type", "")

                # TEXTO DA IA
                if event_type in [
                    "response.text.delta",
                    "response.output_text.delta",
                    "response.output_audio_transcript.delta"
                ]:

                    delta = event.get("delta", "")

                    print(delta, end="", flush=True)

                # terminou resposta
                elif event_type == "response.done":

                    print("\n")
                    break

                # erro
                elif event_type == "error":

                    print("\n❌ ERRO:")
                    print(json.dumps(event, indent=2))
                    break


asyncio.run(main())
