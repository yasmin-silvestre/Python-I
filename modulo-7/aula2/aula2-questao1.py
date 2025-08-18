meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

data = input("Digite uma data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = data.split("/")
mes = int(mes)

print(f"Você nasceu em {dia} de {meses[mes-1]} de {ano}.")
