with open("frase.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()


limpo = ""
for c in conteudo:
    if c.isalpha() or c.isspace():
        limpo += c

palavras = limpo.split()

with open("palavras.txt", "w", encoding="utf-8") as f:
    for palavra in palavras:
        f.write(palavra + "\n")


with open("palavras.txt", "r", encoding="utf-8") as f:
    print(f.read())
