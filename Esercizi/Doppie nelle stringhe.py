import random
parola=input("Inserisci una parola")

doppie=0
for i in range(0,len(parola)-1):
    if parola[i]==parola[i+1]:
        doppie+=1
print("La parola inserita ha:",doppie, "doppie")