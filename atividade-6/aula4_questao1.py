#solicita o comprimento do terreno
comprimento=int(input("Digite o comprimento do terreno em metros:"))

#solicita a largura do terreno
largura=int(input("digite a largura do terreno em metros:"))

#solicita o preço por metro quadrado
preco_m2=float(input("Digite o preço por metro quadrado:"))

#calcula a area do terreno
area_m2= comprimento*largura

#calcula o valor total do terreno
preco_total=preco_m2*area_m2

#exibe resultado:
print(f"O terreno possui {area_m2}m2 e custaa R${preco_total:,.2f}")