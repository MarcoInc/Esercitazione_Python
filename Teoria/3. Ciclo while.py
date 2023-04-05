numero=int(input("Inserisci un valore"))
count=0
print("Adesso conterò fino a",numero)
while count<numero:     #eseguirà il codice dentro il blocco fin quando count rimarrà minore di numero
    print(count+1)      #+1 cosi salto lo 0
    count+=1            #incremento il contatore cosi passo al numero successivo fino al numero scelto
    
#esco dal ciclo while quando la condizione risulterà falsa, ovvero quando il contatore non sarà più minore del numero scelto

print("Inserisci un numero pari")
while True:     #questo ciclo andrà avanti sempre, fin quando non ci sarà un break
    numeroTest=int(input())
    if numeroTest%2==0:         #condizione affinchè un numero sia pari
        print("Bravo, hai inserito un numero pari")
        break                   #se è pari, con un break usciamo dal ciclo while
    else:
        print("Numero dispari. Riprova")        #altrimenti il while ripete nuovamente

#grazie al break, possiamo uscire dal ciclo while ed eseguire questo ultimo messaggio
print("Fine")
    