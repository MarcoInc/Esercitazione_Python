import random
casuale=random.randint(0,2)
if casuale==0:
    semaforo="rosso"
elif casuale==1:
    semaforo="giallo"
elif casuale==2:
    semaforo="verde"
print("il semaforo è "+semaforo)
print("desideri passare?")
risposta=input()
if semaforo=="rosso":
    if risposta=="si":
        print("sei un deficente")
    if risposta=="no":
        print("hai fatto la scelta giusta")

if semaforo=="giallo":
    if risposta=="si":
        print("sbrigati")
    if risposta=="no":
        print("hai fatto bene")

if semaforo=="verde":
    if risposta=="si":
        print("bravo")
    if risposta=="no":
        print("si bestia")