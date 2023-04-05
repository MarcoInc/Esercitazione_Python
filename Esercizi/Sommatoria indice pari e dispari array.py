import random
numeri=[0]*20
for i in range(0,20):
    numeri[i]=random.randint(1,10)
print(numeri)
pospari=0
posdispari=0
for i in range(0,len(numeri)):
    if i%2==0:
        pospari+=numeri[i]
    else:
        posdispari+=numeri[i]
print("somma indice pari:",pospari)
print("somma indice dispari:",posdispari)
        