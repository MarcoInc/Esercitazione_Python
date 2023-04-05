import random
numeri=[0]*50
for i in range(0,50):
    numeri[i]=random.randint(0,50)
print(numeri)
for i in range(0,50):
    if numeri[i]%2==0:
        numeri[i]="pari"
    else:
        numeri[i]="dispari"
print(numeri)
