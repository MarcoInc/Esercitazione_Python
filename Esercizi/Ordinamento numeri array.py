import random
pippo=[0]*100
for i in range(0,100):
    pippo[i]=random.randint(0,100)
print("prima")
print(pippo)
pippo.sort()
print("dopo")
print(pippo)

print(pippo[0])
print(pippo[99])
