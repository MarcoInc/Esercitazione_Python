print("Ciao"*2)     #stampa 2 volte la stringa a sinistra
print("Sinistra"+" "*50+"Destra")   #tra le due stringhe metto 50 spazi

#stampare la stessa print in righe diverse con \n
print("Primo rigo \nSecondo rigo")  #\n indica la fine del rigo di prima e l'inizio di quella che verrà dopo

#rigo vuoto
print("Primo rigo \n\nTerzo rigo")  #dopo aver inserito un rigo, ne inseriamo un altro


#stampa un carattere di tabulazione con \t affinchè si metta un numero fisso di caratteri e incolonnare\indennare meglio il testo
print("Ciao \tMondo")


#unire due stringhe in print diverse
print("Gratta", end="")     #seppur siano in due print separate, con end=""
print("cielo")              #uniamo due stringhe in print separate
                            #la concatenazione avviene mediante il carattere tra le virgolette
                            #in questo caso è un carattere nullo
#inserire uno spazio in due print separate
print("Questa frase è",end=" ")     #il carattere che andremo ad inserire è uno spazio
print("in un solo rigo")            
                                   
#inserire un separatore come una virgola tra due print separate                    
print("Adesso metto una virgola",end=", ")     #concateno le due stringhe usando un separatore
print("visto? Questa è una print separata")            #in questo caso una virgola