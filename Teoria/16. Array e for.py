numeri=[1,5,6,8,2,3]
print("L'array contiene",len(numeri),"elementi")

print("PRIMO METODO")
for i in numeri:        #seleziono i singoli elementi, non gli indici
    print(i)           #stamperà l'elemento i-esimo
    
print("SECONDO METODO")
for i in range(6):          #so che ci sono 6 elementi e quindi seleziono tutti gli indici
    print("Indice")
    print(i)         #stamperà l'indice
    print("Elemento")
    print(numeri[i])    #stamperà l'elemento i-esimo
    
print("ALTERNATIVA AL SECONDO METODO")
for i in range(len(numeri)):  #non so quanto è grande l'array e quindi mi chiedo con len la sua lunghezza
    print(numeri[i])
    
print("SELEZIONE SELETTIVA")
for i in range(0,4):        #seleziona gli indici dall'elemento 0 fino al 4 elemento escluso->quindi fino al 3 indice incluso
    print(numeri[i])

print("SELEZIONE SELETTIVA CON SALTO")
for i in range(0,5,2):  #seleziona gli indici da 0 a 4 ma a 2 a 2 quindi l'elementi agli indici 0, 2 e 4
     print(numeri[i])

