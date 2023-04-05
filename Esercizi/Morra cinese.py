import random 
mossamia=input("fai la tua mossa, s per sasso, f per forbice, c per carta")
casuale=random.randint(0,2)
print("il computer ha pescato")
if casuale==0:
    mossasua="s"
    print("sasso")
if casuale==1:
    mossasua="f"
    print("forbice")
if casuale==2:
    mossasua="c"
    print("carta")

if mossamia==mossasua:
    print("pareggio")
if mossamia=="c" and mossasua=="s" or mossamia=="f" and mossasua=="c" or mossamia=="s" and mossasua=="f":
    print("hai vinto")
if  mossasua=="c" and mossamia=="s" or mossasua=="f" and mossamia=="c" or mossasua=="s" and mossamia=="f":
    print("hai perso")