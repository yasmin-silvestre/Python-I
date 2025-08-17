import random
lista = [random.randint(-10, 10) for _ in range(20)]
print("Lista original:", lista)

maior_inicio, maior_fim = -1, -1
atual_inicio, atual_fim = -1, -1

for i, num in enumerate(lista):
    if num < 0:  # se for negativo
        if atual_inicio == -1:
            atual_inicio = i
        atual_fim = i
    else:
        if atual_inicio != -1:
            # Verifica se intervalo atual é maior que o maior até agora
            if maior_inicio == -1 or (atual_fim - atual_inicio) > (maior_fim - maior_inicio):
                maior_inicio, maior_fim = atual_inicio, atual_fim
            atual_inicio, atual_fim = -1, -1

# Checagem final se terminou em intervalo negativo
if atual_inicio != -1 and (maior_inicio == -1 or (atual_fim - atual_inicio) > (maior_fim - maior_inicio)):
    maior_inicio, maior_fim = atual_inicio, atual_fim
# Apagar intervalo
if maior_inicio != -1:
    del lista[maior_inicio:maior_fim+1]

print("Lista editada:", lista)
