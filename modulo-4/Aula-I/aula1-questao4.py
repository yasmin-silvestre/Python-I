n=int(input("digite um valor: "))
maior=0
while n>0:
    x=int(input("digite um valor para x"))
    if x>maior:
        maior=x
    n=n-1
print(maior)