print("inserisci la data di oggi")
giorno=int(input("giorno"))
mese=int(input("mese"))
anno=int(input("anno"))

print("inserisci la data di qualcuno")
giornotizio=int(input("giorno"))
mesetizio=int(input("mese"))
annotizio=int(input("anno"))
if anno-annotizio<18:
    print("minorenne")
elif anno-annotizio>18:
    print("maggiorenne")
elif anno-annotizio==18:
    if mesetizio<mese:
        print("maggiorenne")
    elif mesetizio>mese:
        print("minorenne")
    elif mesetizio==mese:
        if giornotizio<=giorno:
            print("maggiorenne")
        elif giornotizio>giorno:
            print("minorenne")
