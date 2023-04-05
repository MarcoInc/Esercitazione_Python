#STRINGA MULTILINEA
stringa = """Nel mezzo del cammin di nostra vita        
mi ritrovai per una selva oscura,               
ché la diritta via era smarrita."""
print(stringa)      #il risultato sarà una print che rispetta gli "a capo" 

#LUNGHEZZA STRINGA
print("LA STRINGA È LUNGA",len(stringa),"CARATTERI")    #la funzione ci da il numero di caratteri della stringa

    
#SOTTOSTRINGA       #estrarre una parte di una stringa
print("LA SOTTOSTRINGA DAL 14ESIMO CARATTERE INCLUSO AL 25ESIMO NON INCLUSO:")
print(stringa[14:19])       #estraee dal primo indice incluso all'ultimo indice escluso

#SOTTOSTRINGA DALL'INIZIO
print("I PRIMI 25 CARATTERI (FINO AL 24ESIMO):")
print(stringa[:25])         #estraee dal primo al 25esimo carattero non incluso, quindi al 24

#SOTTOSTRINGA DALLA FINE
print("GLI ULTIMI CARATTERI DAL 100ESIMO:")
print(stringa[100:])        #estraee le dal 100esimo carattere fino alla fine della stringa
    
