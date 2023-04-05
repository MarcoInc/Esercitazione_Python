import random
lotto1=random.randint(1,61)
lotto2=random.randint(1,61)
lotto3=random.randint(1,61)
lotto4=random.randint(1,61)
lotto5=random.randint(1,61)
print("estratti",lotto1,lotto2,lotto3,lotto4,lotto5)
numero1=input("primo numero")
numero2=input("secondo numero")
numero3=input("terzo numero")
numero4=input("quarto numero")
numero5=input("quinto numero")

indovinati=0
if numero1==lotto1 or numero1==lotto2 or numero1==lotto3 or numero1==lotto4 or numero1==lotto5:
    indovinati=indovinati+1
if numero2==lotto1 or numero2==lotto2 or numero2==lotto3 or numero2==lotto4 or numero2==lotto5:
    indovinati=indovinati+1
if numero3==lotto1 or numero3==lotto2 or numero3==lotto3 or numero3==lotto4 or numero3==lotto5:
    indovinati=indovinati+1
if numero4==lotto1 or numero4==lotto2 or numero4==lotto3 or numero4==lotto4 or numero4==lotto5:
    indovinati=indovinati+1
if numero5==lotto1 or numero5==lotto2 or numero5==lotto3 or numero5==lotto4 or numero5==lotto5:
    indovinati=indovinati+1
print("indovinati",indovinati)


