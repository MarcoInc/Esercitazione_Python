from random import *
numero=randint(1,10)
tentativi=0
while True:
    mionumero=int(input("Inserisci un numero"))
    if mionumero<numero:
        tentativi+=1
        print("Hai inserito un numero piccolo")
    if mionumero>numero:   
        tentativi+=1
        print("Hai inserito un numero grande")
    if mionumero==numero:
        print("Hai indovinato in",tentativi,"tentativi")
        break
        