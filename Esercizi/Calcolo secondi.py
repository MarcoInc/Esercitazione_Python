giorni = int(input("Inserisci il numero di giorni: ")) 
secGiorni=giorni* 24 * 3600
ore = int(input("Inserisci il numero di ore: ")) 
secOre=ore*3600
minuti = int(input("Inserisci il numero di minuti: ")) 
secMinuti=minuti*60
totale = secGiorni + secOre + secMinuti
print("Secondi in totale:",totale)