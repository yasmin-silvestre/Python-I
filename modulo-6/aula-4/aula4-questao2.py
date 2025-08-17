
frase = input("Digite uma frase: ")

vogais = sorted([ch for ch in frase if ch.lower() in "aeiou"])
consoantes = [ch for ch in frase if ch.isalpha() and ch.lower() not in "aeiou"]

print("Vogais:", vogais)
print("Consoantes:", consoantes)
