import random
numeri=[0]*20
for i in range(0,20):
    numeri[i]=random.randint(1,20)
print(numeri)
controllo=int(input("Quale numero vuoi cercare?"))
sostituzione=input("Con cosa vuoi sostituire?")

for i in range(0,20):
    if numeri[i]==controllo:
        numeri[i]=sostituzione
print(numeri)
        
        

