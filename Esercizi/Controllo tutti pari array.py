import random
numeri=[0]*5
for i in range(0,5):
    numeri[i]=random.randint(1,5)
print(numeri)
contatore=0
for i in range(0,len(numeri)):
    if numeri[i]%2==0:
        contatore+=1
        
if contatore==len(numeri):
    print("sono tutti pari")
else:
    print("sono tutti dispari")
        