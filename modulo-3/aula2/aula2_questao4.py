# Solicita a classe do personagem
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")

# Solicita os pontos de força e magia
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# Inicializa a variável de validação
valido = False

# Regras por classe
if classe == "guerreiro":
    valido = (forca >= 15) and (magia <= 10)
elif classe == "mago":
    valido = (forca <= 10) and (magia >= 15)
elif classe == "arqueiro":
    valido = (forca > 5) and (magia > 5) and (forca <= 15) and (magia <= 15)

print("Pontos de atributo consistentes com a classe escolhida:", valido)
