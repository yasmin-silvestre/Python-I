# Solicita as idades novamente
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

# Verifica se pelo menos uma tem mais de 17 anos
podem_entrar = (idade_juliana > 17) or (idade_cris > 17)

# Imprime True ou False
print(podem_entrar)
