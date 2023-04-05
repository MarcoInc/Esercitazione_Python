import random
numeri=[0]*5
for i in range(0,5):
    numeri[i]=random.randint(0,1000000000)
    print("numeri:",numeri[i])
for i in range(0,4):
    if numeri[i]>numeri[i+1]:
        print("non è ordinato")
        break