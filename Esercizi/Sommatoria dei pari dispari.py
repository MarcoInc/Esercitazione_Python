print("inserisci primo numero")
sommapari=0
sommadispari=0
for i in range(0,10):
    numero=int(input())
    if numero%2==0:
       sommapari+=numero
    else:
        sommadispari+=numero
print("somma dei pari",sommapari)
print("somma dei dispari",sommadispari)
    
       