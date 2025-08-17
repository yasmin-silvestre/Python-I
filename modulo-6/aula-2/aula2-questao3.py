import random

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = sorted(set(lista1) & set(lista2))

contagem = {x: (lista1.count(x), lista2.count(x)) for x in interseccao}

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção:", interseccao)
print("Contagem:")
for k, (c1, c2) in contagem.items():
    print(f"{k}: (lista1={c1}, lista2={c2})")
