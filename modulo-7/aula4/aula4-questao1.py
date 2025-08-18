

import os

frase = input("Digite uma frase: ")
caminho = os.path.abspath("frase.txt")

with open("frase.txt", "w", encoding="utf-8") as f:
    f.write(frase)

print("Frase salva em", caminho)
