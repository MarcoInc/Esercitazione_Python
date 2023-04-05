from random import *        #necessario per generare numeri random
quantita=int(input("Quanti numeri vuoi generare?"))
count=0
print("Eccoti i numeri",quantita,"numeri richiesti")
while count<quantita:
    numero=randint(1,10000)
    print(numero)
    count+=1