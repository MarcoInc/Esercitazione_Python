altezza=int(input("inserisci l'altezza della montagna"))
contatore=1 
while contatore<=altezza:
    print("@"*contatore)
    contatore+=1
while contatore>=0:
    print("@"*contatore)
    contatore-=1