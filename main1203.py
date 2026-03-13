from datetime import datetime
from pathlib import Path

caminho = Path("relatorio.txt")

agora = datetime.now()
agora_formatado = agora.strftime("Arquivo criado em %d/%m/%Y às %H:%M")
with open(caminho, 'w', encoding='utf-8') as arquivo:
    arquivo.write(f"Estou aprendendo programação em linguagem Python!\n{agora_formatado}\n")

