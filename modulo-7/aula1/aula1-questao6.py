frase = input("Digite uma frase: ").split()
objetivo = input("Digite a palavra objetivo: ")

anagramas = [palavra for palavra in frase if sorted(palavra.lower()) == sorted(objetivo.lower())]
print("Anagramas:", anagramas)
