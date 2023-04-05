import random
numeri=[0]*20
for i in range(0,20):
    numeri[i]=random.randint(1,20)
print(numeri)
max=int(input("Fin quando vuoi controllare"))
contatore=0
for i in range(0,len(numeri)):
    if numeri[i]<=max:
            contatore+=1

print("ce ne sono ",contatore)

        