n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input()) for _ in range(n1)]

n2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = [int(input()) for _ in range(n2)]

lista_intercalada = []
for i in range(min(n1, n2)):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])
if n1 > n2:
    lista_intercalada.extend(lista1[n2:])
else:
    lista_intercalada.extend(lista2[n1:])

print("Lista intercalada:", lista_intercalada)
