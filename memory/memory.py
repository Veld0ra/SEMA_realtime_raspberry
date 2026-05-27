import os
from datetime import datetime, date
from collections import deque


class Memory:
    def __init__(self):
        # memória curta (20 mensagens)
        self.buffer = deque(maxlen=20)

        # caminhos
        self.base_path = "memory/data"
        self.conversas_path = os.path.join(self.base_path, "conversas")
        self.persistente_path = os.path.join(self.base_path, "persistente")

        os.makedirs(self.conversas_path, exist_ok=True)
        os.makedirs(self.persistente_path, exist_ok=True)

        self.arquivo_dia = self._get_daily_file()

    # ----------------------------
    # ARQUIVO DO DIA
    # ----------------------------
    def _get_daily_file(self):
        hoje = date.today().isoformat()
        return os.path.join(self.conversas_path, f"{hoje}.md")

    def iniciar_dia(self):
        if not os.path.exists(self.arquivo_dia):
            with open(self.arquivo_dia, "w", encoding="utf-8") as f:
                f.write(f"# Conversa do dia {date.today().isoformat()}\n\n")

    # ----------------------------
    # MEMÓRIA CURTA
    # ----------------------------
    def add_buffer(self, role, text):
        self.buffer.append((role, text))

    def get_buffer(self):
        return list(self.buffer)

    # ----------------------------
    # MEMÓRIA DIÁRIA
    # ----------------------------
    def salvar_conversa(self, role, text):
        hora = datetime.now().strftime("%H:%M")

        with open(self.arquivo_dia, "a", encoding="utf-8") as f:
            f.write(f"### {hora} - {role}\n{text}\n\n")

    # ----------------------------
    # MEMÓRIA PERSISTENTE
    # ----------------------------
    def salvar_memoria_fixa(self, nome, conteudo):
        path = os.path.join(self.persistente_path, f"{nome}.md")

        with open(path, "w", encoding="utf-8") as f:
            f.write(conteudo)

    def ler_memoria_fixa(self):
        textos = []

        # 🔥 AGORA LÊ TODAS AS SUBPASTAS
        for root, dirs, files in os.walk(self.persistente_path):
            for file in files:
                if file.endswith(".md"):
                    path = os.path.join(root, file)

                    with open(path, "r", encoding="utf-8") as f:
                        textos.append(f.read())

        return "\n\n".join(textos)
