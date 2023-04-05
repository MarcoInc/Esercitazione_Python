import random
numeri=[0]*20
for i in range(0,20):
    numeri[i]=random.randint(1,20)
print(numeri)
primaposizione=int(input("inserisci la posizione del primo numero da scambiare"))
secondaposizione=int(input("inserisci la posizione del secondo numero da scambiare"))

temporaneo=numeri[primaposizione]
numeri[primaposizione]=numeri[secondaposizione]
numeri[secondaposizione]=temporaneo

print(numeri)
        
        

