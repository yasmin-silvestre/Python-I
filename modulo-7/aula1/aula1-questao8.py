cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ").replace(".", "").replace("-", "")

if len(cpf) != 11 or not cpf.isdigit():
    print("Inválido")
else:
    # Primeiro dígito
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    dig1 = 0 if resto < 2 else 11 - resto

    # Segundo dígito
    soma = sum(int(cpf[i]) * (11 - i) for i in range(9)) + dig1 * 2
    resto = soma % 11
    dig2 = 0 if resto < 2 else 11 - resto

    if cpf[-2:] == f"{dig1}{dig2}":
        print("Válido")
    else:
        print("Inválido")
