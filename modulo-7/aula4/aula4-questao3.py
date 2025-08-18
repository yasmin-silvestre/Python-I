with open("estomago.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()

print("===== Primeiras 25 linhas =====")
for l in linhas[:25]:
    print(l.strip())

print("\nNúmero de linhas:", len(linhas))

maior = max(linhas, key=len)
print("\nLinha com maior número de caracteres:")
print(maior.strip())

texto = "".join(linhas).lower()
n_nonato = texto.count("nonato")
n_iria = texto.count("íria")

print(f"\nMenções a Nonato: {n_nonato}")
print(f"Menções a Íria: {n_iria}")
