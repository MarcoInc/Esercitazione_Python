numero1=input("primo numero")
numero2=input("secondo numero")
numero3=input("terzo numero")
numero4=input("quarto numero")

if numero1>numero2:
    max=numero1
else:
    max=numero2
if numero2>max:
    max=numero2
if numero3>max:
    max=numero3
if numero4>max:
    max=numero4
print("max",max)
    
if numero1<numero2:
    min=numero1
else:
    min=numero2
if numero2<min:
    min=numero2
if numero3<min:
    min=numero3
if numero4<min:
    min=numero4
print("min",min)
    
