print("Inserisci 10 numeri")
sommaPari=0
sommaDispari=0
for i in range(0,10):
    numero=int(input())
    if numero%2==0:
        sommaPari+=numero
    else:
        sommaDispari+=numero
    
print("Somma pari",sommaPari)
print("Somma dispari",sommaDispari)
