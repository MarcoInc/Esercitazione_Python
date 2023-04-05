import random
numeri=[0]*20
for i in range(0,20):
    numeri[i]=random.randint(1,10)
print(numeri)
pari=0
dispari=0
for i in range(0,len(numeri)):
    if numeri[i]%2==0:
        pari+=numeri[i]
    else:
        dispari+=numeri[i]
print("somma pari:",pari)
print("somma dispari:",dispari)
        