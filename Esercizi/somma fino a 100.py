numeri=[]
somma=0
print("inserisci dei valori, mi fermo quando arrivo a 100 come somma")
while True:
    numero=int(input())
    numeri.append(numero)
    somma+=numero
    if somma>=100:
        break
print("finito")
print(numeri)
    