# Inicializando contadores
total_cobaias = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

# Lendo número de experimentos
N = int(input("Digite o número de experimentos registrados: "))

# Processando cada experimento
for i in range(1, N + 1):
    entrada = input(f"Experimento {i} - Digite a quantidade de cobaias e o tipo (S, R ou C), separados por espaço: ").split()
    quantia = int(entrada[0])
    tipo = entrada[1]
    
    total_cobaias += quantia
    
    if tipo == 'S':
        total_sapos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'C':
        total_coelhos += quantia

# Calculando percentuais
percent_sapos = (total_sapos / total_cobaias) * 100
percent_ratos = (total_ratos / total_cobaias) * 100
percent_coelhos = (total_coelhos / total_cobaias) * 100

# Exibindo resultados
print(f"\nTotal: {total_cobaias} cobaias")
print(f"Total de sapos: {total_sapos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de coelhos: {total_coelhos}")
print(f"Percentual de sapos: {percent_sapos:.2f} %")
print(f"Percentual de ratos: {percent_ratos:.2f} %")
print(f"Percentual de coelhos: {percent_coelhos:.2f} %")


