
numeros = []
print("Digite números inteiros (digite 'fim' para parar, mínimo de 4 números):")
while True:
    entrada = input()
    if entrada.lower() == "fim":
        if len(numeros) < 4:
            print("Digite pelo menos 4 números antes de parar!")
            continue
        break
    try:
        numeros.append(int(entrada))
    except ValueError:
        print("Entrada inválida, digite um número ou 'fim'.")


print("Lista original:", numeros)
print("3 primeiros elementos:", numeros[:3])
print("2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])
