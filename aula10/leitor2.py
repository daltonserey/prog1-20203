import sys

n = int(sys.argv[1])
problema = sys.argv[2]

# repetir 5 vezes:
contagem = 0
for i in range(n):
    nome_arquivo = input()
    if (problema in nome_arquivo) and (not nome_arquivo.endswith(".json")):
        print(f"ocorrência na linha {i + 1}")
        contagem += 1

print(f"{contagem} alunos fizeram a atividade area_circulo_2")
