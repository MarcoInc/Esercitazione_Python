import random
contatore1=0
contatore2=0
for i in range(1,6):
    lancio=random.randint(0,1)
    if lancio==0:
        print("testa")
        contatore1+=1
    if lancio==1:
        print("croce")
        contatore2+=1
print("testa",contatore1)
print("croce",contatore2)

