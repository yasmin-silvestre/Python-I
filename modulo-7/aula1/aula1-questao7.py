import random

def encrypt(nomes):
    n = random.randint(1, 10)  # chave aleatória
    cript = []
    for nome in nomes:
        novo = ""
        for c in nome:
            codigo = ord(c) + n
            if codigo > 126:  # mantém dentro da faixa visível
                codigo = 33 + (codigo - 127)
            novo += chr(codigo)
        cript.append(novo)
    return cript, n

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
cript, chave = encrypt(nomes)

print("Nomes criptografados:", cript)
print("Chave:", chave)
