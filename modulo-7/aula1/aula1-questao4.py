
numero = input("Digite o número: ")

if len(numero) == 8:   # só 8 dígitos → acrescenta 9
    numero = "9" + numero
elif len(numero) == 9 and numero[0] != "9":  # tem 9 mas não começa com 9
    numero = "9" + numero[1:]

print(f"Número completo: {numero[:5]}-{numero[5:]}")
