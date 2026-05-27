# core/receiver.py
import json


async def receber_resposta(ws):
    """
    Fica escutando eventos do Realtime e imprime o texto da resposta.
    Para quando a resposta termina (response.done).
    """

    while True:
        raw = await ws.recv()
        event = json.loads(raw)

        event_type = event.get("type", "")

        # textos da IA
        if event_type in [
            "response.text.delta",
            "response.output_text.delta",
            "response.output_audio_transcript.delta"
        ]:
            delta = event.get("delta", "")
            print(delta, end="", flush=True)

        # fim da resposta
        elif event_type == "response.done":
            print()
            break

        # erro
        elif event_type == "error":
            print("\n❌ ERRO:", json.dumps(event, indent=2))
            break


