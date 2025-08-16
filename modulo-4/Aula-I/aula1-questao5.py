N = int(input("Digite a quantidade de respondentes: "))

soma = 0
for i in range(N):
    idade = int(input(f"Digite a idade do respondente {i+1}: "))
    soma += idade

media = soma / N
print(f"A média das idades é: {media:.2f}")
