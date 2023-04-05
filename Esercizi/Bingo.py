from random import *
numero1=int(input("inserisci il primo numero"))
numero2=int(input("inserisci il secondo numero"))
numero3=int(input("inserisci il terzonumero"))
numero4=int(input("inserisci il quarto numero"))
numero5=int(input("inserisci il quinto numero"))
numero6=int(input("inserisci il sesto numero"))
numero7=int(input("inserisci il settimo numero"))
numero8=int(input("inserisci il ottavo numero"))
numero9=int(input("inserisci il nono numero"))
numero10=int(input("inserisci il decimo numero"))

numeroavversario1=randint(1,100)
numeroavversario2=randint(1,100)
numeroavversario3=randint(1,100)
numeroavversario4=randint(1,100)
numeroavversario5=randint(1,100)
numeroavversario6=randint(1,100)
numeroavversario7=randint(1,100)
numeroavversario8=randint(1,100)
numeroavversario9=randint(1,100)
numeroavversario10=randint(1,100)

print("tuoi numeri" , numero1,numero2,numero3,numero4,numero5,numero6,numero7,numero8,numero9,numero10)
print("numeri avversario", numeroavversario1,numeroavversario2,numeroavversario3,numeroavversario4,numeroavversario5,numeroavversario6,numeroavversario7,numeroavversario8,numeroavversario9,numeroavversario10)

contatoremio=0
contatoreavversario=0
while True:
    casuale=randint(1,100)
    if casuale==numeroavversario1  or casuale==numeroavversario2  or casuale==numeroavversario3  or casuale==numeroavversario4  or casuale==numeroavversario5 or casuale==numeroavversario6  or casuale==numeroavversario7  or casuale==numeroavversario8  or casuale==numeroavversario9  or casuale==numeroavversario10:
        contatoreavversario+=1  
        if contatoreavversario==10:
            print("hai perso")
            print("tuo punteggio",contatoremio)
            break
    if casuale==numero1  or casuale==numero2  or casuale==numero3  or casuale==numero4  or casuale==numero5 or casuale==numero6  or casuale==numero7  or casuale==numero8  or casuale==numero9  or casuale==numero10:
        contatoremio+=1  
        if contatoremio==10:
            print("hai vinto")
            print("punteggio avversario",contatoreavversario)
            break
        
        
        
        

