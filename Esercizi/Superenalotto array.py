from random import *        #libreria per usare numeri random
numeriScelti=[0,0,0,0,0]    #creo un array di soli 0
for i in range(5):          #scorro tutti e 5 elementi dell'array
    print("Inserisci il",i+1,"° numero della tua schedina")
    numeriScelti[i]=int(input())    #chiedo all'utente di inserire un valore dell'i-esimo elemento
    
numeriEstratti=[0,0,0,0,0]
print("Numeri estratti:")
for i in range(5):
    numeriEstratti[i]=randint(1,61) #i-esimo elemento avrà un valore random compreso tra 1 e 60
    print(numeriEstratti[i])
    
contatore=0             #contatore che terrà conto dei numeri indovinati
for i in range(5):      #scorro l'array numeriSceltiScelti con indice i 
        for j in range(5):      #scorro l'array numeriEstratti con indice j
            if numeriScelti[i]==numeriEstratti[j]:      #confronto elementi i-esimo con l'elemento j-esimo
                contatore+=1                    #se ho beccato un numero incremento il contatore
print("Hai indovinato",contatore,"numeri")

