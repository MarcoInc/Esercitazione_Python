misura=["km","hm","dam","m","dm","cm","mm"]
misuraPartenza=input("da dove vuoi convertire? (km,hm,dam,m,dm,cm,mm)")
misuraDestinazione=input("a cosa vuoi convertire? (km,hm,dam,m,dm,cm,mm)")
numero=float(input("quanto hai misurato"))

indicePartenza=misura.index(misuraPartenza)
indiceDestinazione=misura.index(misuraDestinazione)

distanza=abs(indicePartenza-indiceDestinazione)
moltiplicatore=1 
for i in range(0,distanza):
    moltiplicatore*=10


if indicePartenza>indiceDestinazione:
    risultato=numero/moltiplicatore
elif indicePartenza<indiceDestinazione:
    risultato=numero*moltiplicatore
elif  indicePartenza==indiceDestinazione:
    risultato=numero*1
print(risultato)
    
    
