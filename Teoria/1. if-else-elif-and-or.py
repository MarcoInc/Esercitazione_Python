numero=int(input("Inserisci un valore"))
if numero%2==0:
    print("Il numero è pari")
else:
    print("Il numero è dispari")

if numero>0 and numero<50:      #and rende vera la condizione solo se entrambe sono vere
    print("Il numero è compreso tra 0 e 50")
elif numero>=50 and numero<=100:
    print("Il numero è compreso tra 50 e 100")
else:
    print("Il numero è più grande di 100 o è negativo")

if numero%3==0 or numero%2==0:  #or rende vera la condizione basta che c'è ne sia una vera
    print("Il numero o pari o divisibile per 3 o entrambi")