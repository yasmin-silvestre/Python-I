# Solicita o gênero do usuário
genero = input("Digite seu gênero (M ou F): ")

# Solicita a idade
idade = int(input("Digite sua idade: "))

# Solicita o tempo de serviço
tempo_servico = int(input("Digite seu tempo de serviço (anos): "))

# Verifica condições para aposentadoria
pode_aposentar = False

# Condições A
if (genero == "F" and idade > 60) or (genero == "M" and idade > 65):
    pode_aposentar = True

# Condição B
elif tempo_servico >= 30:
    pode_aposentar = True

# Condição C
elif idade >= 60 and tempo_servico >= 25:
    pode_aposentar = True

print(pode_aposentar)
