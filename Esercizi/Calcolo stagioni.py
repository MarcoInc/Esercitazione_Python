giorno=int(input("inserisci un giorno"))
mese=input("inserisci un mese")
if mese=="aprile" or mese=="maggio":
    stagione="primavera"
if mese=="luglio" or mese=="agosto":
    stagione="estate"
if mese=="ottombre" or mese=="novembre":
    stagione="autunno"
if mese=="gennaio" or mese=="febbraio":
    stagione="inverno"
    
if mese=="marzo":
    if giorno<=20:
        stagione="inverno" 
    if giorno>20:
        stagione="primavera"
if mese=="giugno":
    if giorno<=20:
        stagione="primavera" 
    if giorno>20:
        stagione="estate"
if mese=="settembre":
    if giorno<=22:
        stagione="estate" 
    if giorno>22:
        stagione="autunno"
if mese=="dicembre":
    if giorno<=21:
        stagione="autunno" 
    if giorno>21:
        stagione="inverno"
    stagione="inverno"
print("la stagione è "+stagione)
