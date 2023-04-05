n = int(input('Inserisci un numero n: '))
for i in range(1,n+1): # l'ultimo indice e' escluso!
    for j in range(1,i+1): # l'ultimo indice e' escluso!
        print (j,end=" ")
    print("")
