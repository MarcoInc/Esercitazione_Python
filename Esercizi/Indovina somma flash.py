import random
punteggio=0
for i in range(0,5):
    casuale1=random.randint(0,100)
    casuale2=random.randint(0,100)
    print(casuale1, " ",casuale2)
    risposta=int(input("secondo te qual'è la somma"))
    if risposta==casuale1+casuale2:
        print("hai indovinato")
        punteggio+=1
    else:
        print("hai sbagliato")
print("punteggio",punteggio)
    
