numero1=float(input("inserisci il primo numero"))
numero2=float(input("inserisci il secondo numero"))
if numero1%2==0 or numero2%2==0:
    print(numero1+numero2)
elif numero1%2==0 and numero2%2==0:
    print(numero1*numero2)
elif numero1%2==1 and numero2%2==1:
    print(numero1/numero2)