import random

num_elementos = random.randint(5, 20)

elementos = [random.randint(1, 10) for _ in range(num_elementos)]

soma = sum(elementos)
media = soma / len(elementos)

print("Lista de elementos:", elementos)
print("Soma:", soma)
print("Média:", media)
