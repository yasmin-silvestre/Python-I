# Solicita ao usuário a temperatura em Fahrenheit
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))

# Converte a temperatura para Celsius com a fórmula
celsius = (fahrenheit - 32) * (5 / 9)

# Converte o valor de Celsius para inteiro
celsius_inteiro = int(celsius)

# Exibe o resultado formatado
print(f"{fahrenheit} graus Fahrenheit são {celsius_inteiro} graus Celsius.")
