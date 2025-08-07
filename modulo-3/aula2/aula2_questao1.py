# Solicita a idade de Juliana
idade_juliana = int(input("Digite a idade de Juliana: "))

# Solicita a idade de Cris
idade_cris = int(input("Digite a idade de Cris: "))

# Verifica se ambas têm idade maior que 17
podem_entrar = (idade_juliana > 17) and (idade_cris > 17)

# Imprime True ou False
print(podem_entrar)
