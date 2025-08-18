import string

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == "fim":
        break

    # remove espaços, pontuação e coloca tudo em minúsculo
    limpa = "".join(ch.lower() for ch in frase if ch.isalnum())

    if limpa == limpa[::-1]:
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
