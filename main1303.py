from pathlib import Path


# # exercicio 2
# caminho = Path("mensagem.txt")

# with open(caminho, 'r', encoding='utf-8') as arquivo:
#     contador = 0
#     for letra in arquivo.read():
#         if letra.isalpha():
#             contador += 1
#     print(f'O texto contém {contador} letras')

# # exercicio 3
# caminho = Path("acesso.log")

# with open(caminho, 'r', encoding='utf-8') as arquivo:
#     for palavras in arquivo.readlines():
#         if "ERROR" in palavras or 'INFO' in palavras or 'WARNING' in palavras:
#             print(palavras)



# # exercicio 4

caminho = Path("tarefas.txt")

with open(caminho, 'w+', encoding='utf-8') as arquivo:
    tarefas = []
    for i in range(3):
        tarefa = input("Digite as 3 tarefas que deseja guardar")
        tarefas.append(tarefa)

    arquivo.write(tarefas).strip()
    arquivo.seek(0)
    print(f'Suas tarefas são:\n{arquivo.read()}')



