idade=int(input("digite sua idade:"))
quantidade_jogos=input("já jogou mais de 3 jogos? (responda com true ou false)")
if quantidade_jogos=="true":
   quantidade_jogos=True
vezes_vencidas=int(input("quantas vezes venceu um jogo?"))
if 19>idade>15 and quantidade_jogos and vezes_vencidas>0:
     print("Você esta apto para o clube!")
else:
     print("você não esta apto para o clube!")