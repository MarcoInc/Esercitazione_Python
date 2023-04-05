spazio=float(input("quanti km hai percorso?"))
tempo=float(input("in quante ore?"))
v=spazio/tempo
print("velocità rilevata", v,"km/h")
if v>=120:
    print("troppo veloce")
elif v>=80 and v<120:
    print("rallenta bestia")
elif v>=20 and v<80:
    print("ok")
elif v>0 and v<20:
    print("spicciti")
