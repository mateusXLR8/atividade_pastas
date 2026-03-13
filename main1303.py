from pathlib import Path

caminho = Path("mensagem.txt")

with open(caminho, 'r', encoding='utf-8') as arquivo:
    contador = 0
    for letra in arquivo.read():
        if letra.isalpha():
            contador += 1
    print(f'O texto contém {contador} letras')

