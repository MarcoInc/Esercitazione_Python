numeri=[]
contatore=0
for i in range(5):
    numeri.append(int(input()))
    print("numero inserito",numeri[i])
    if numeri[i] < 10:
        contatore=contatore+1
print("i numeri minori di 10 sono",contatore)