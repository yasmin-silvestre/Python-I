# Solicita os dados do produto 1
produto1 = input("Digite o nome do produto 1:")
preco1 = float(input("Digite o preço unitário do produto 1:"))
quant1 = int(input("Digite a quantidade do produto 1: "))

# Solicita os dados do produto 2
produto2 = input("Digite o nome do produto 2:")
preco2 = float(input("Digite o preço unitário do produto 2:"))
quant2 = int(input("Digite a quantidade do produto 2: "))

# Solicita os dados do produto 3
produto3 = input("Digite o nome do produto 3:")
preco3 = float(input("Digite o preço unitário do produto 3:"))
quant3 = int(input("Digite a quantidade do produto 3: "))

# Calcula o total da compra
total = (preco1 * quant1) + (preco2 * quant2) + (preco3 * quant3)

# Exibe o total formatado com separador de milhar e duas casas decimais
print(f"Total: R${total:,.2f}")
