import random

# carregar palavras
with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = [p.strip() for p in f.readlines()]

# carregar enforcado
with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
    estagios = f.read().split("\n\n")

def imprime_enforcado(erros):
    print(estagios[erros])

palavra = random.choice(palavras).lower()
progresso = ["_" for _ in palavra]
erros = 0
tentativas = set()

print("Jogo da Forca!")
while erros < 6 and "_" in progresso:
    print(" ".join(progresso))
    letra = input("Digite uma letra: ").lower()

    if letra in tentativas:
        print("Você já tentou essa letra!")
        continue
    tentativas.add(letra)

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                progresso[i] = letra
    else:
        erros += 1
        imprime_enforcado(erros)

if "_" not in progresso:
    print("Parabéns! Você acertou:", palavra)
else:
    print("Você perdeu! A palavra era:", palavra)
