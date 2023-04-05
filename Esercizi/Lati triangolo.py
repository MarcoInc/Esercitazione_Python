lato1=int(input("Inserisci il primo lato di un triangolo: "))
lato2=int(input("Inserisci il secondo lato di un triangolo: "))
lato3=int(input("Inserisci il terzo lato di un triangolo: "))

if lato1==lato2 and lato2==lato3:
    print("Il triangolo è equilatero")
    
elif lato1==lato2 or lato2==lato3 or lato3==lato1:
    print("Il triangolo è isoscele")
    
else:
    print("Il triangolo è scaleno")


