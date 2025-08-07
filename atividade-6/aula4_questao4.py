# Solicita o valor em reais
valor = int(input())

# Lista das notas disponíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Para cada tipo de nota, calcula quantas são necessárias
for nota in notas:
    qtd = valor // nota  # Divide o valor atual pela nota
    print(f"{qtd} nota(s) de R${nota},00")
    valor = valor % nota  # Atualiza o valor restante
1