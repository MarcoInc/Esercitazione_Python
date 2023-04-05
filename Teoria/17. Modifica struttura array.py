numeri=[1,5,7]
print("Prima di append()")      #stampo l'array prima di modificarlo
for i in range(len(numeri)):
    print(i,") ",numeri[i])
#NOME_ARRAY.append(COSA AGGIUNGERE)
numeri.append(10000)        #aggiungo un elemento alla fine dell'array, che diventerà l'ultimo elemento
print("Dopo di append()")
for i in range(len(numeri)):    #array avrà la dimensione aumentata di 1
    print(i,") ",numeri[i])
#NOME_ARRAY.insert(INDICE,COSA AGGIUNGERE NELL'INDICE)
numeri.insert(2, 2000)          #aggiungo 2000 nella posizione 2, il vecchio elemento in posizione 2 passerà alla posizione 3
print("Dopo di insert()")
for i in range(len(numeri)):    #array avrà la dimensione aumentata di 1
    print(i,") ",numeri[i])
#NOME_ARRAY.pop(INDICE DA ELIMINARE)
numeri.pop(0)                    #verrà eliminato l'elemento all'indice specificiato tra parentesi, l'elemento successivo prenderà il posto di quello eliminato
print("Dopo di pop()")
for i in range(len(numeri)):      #array avrà la dimensione diminuita di 1  
    print(i,") ",numeri[i])
