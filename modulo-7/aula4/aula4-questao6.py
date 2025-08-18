# Exercício 6 - Spotify músicas mais tocadas por ano

import csv

mais_tocadas = {}

with open("spotify-2023.csv", "r", encoding="latin-1") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        try:
            ano = int(linha["released_year"])
            if 2012 <= ano <= 2022:
                track = linha["track_name"]
                artist = linha["artist(s)_name"]
                streams = int(linha["streams"])
                if (ano not in mais_tocadas) or (streams > mais_tocadas[ano][3]):
                    mais_tocadas[ano] = [track, artist, ano, streams]
        except:
            # ignora linhas mal formatadas (aspas extras etc.)
            continue

# ordenar por ano e imprimir lista
resultado = [mais_tocadas[ano] for ano in sorted(mais_tocadas)]
print(resultado)
