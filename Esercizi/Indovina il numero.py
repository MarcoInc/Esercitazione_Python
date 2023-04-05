from random import *
casuale=randint(1,10)
tentativi=0
while True: 
    numeroscelto=int(input("inserisci un numero"))
    if numeroscelto==casuale:
        print("indovinato")
        print("tentativi", tentativi)
        break
        
    if numeroscelto<casuale:
        print("troppo piccolo")
        tentativi+=1
    
    if numeroscelto>casuale:
        print("troppo grande")
        tentativi+=1