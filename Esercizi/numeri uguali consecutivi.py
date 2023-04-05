import random
numeri=[0]*20
for i in range(0,20):
    numeri[i]=random.randint(1,10)
print(numeri)
doppi=0
for i in range(0,len(numeri)-1):
    if numeri[i]==numeri[i+1]:
        doppi+=1
print(doppi)