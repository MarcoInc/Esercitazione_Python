array=["scarpe", "TelEfono", "AZZURRO", "spIaGGia","bandana"]
print(array)
minuscole=0
maiuscole=0
for i in range(0,5):
    if array[i].isupper():
        maiuscole+=1
    if array[i].islower():
        minuscole+=1
print("le maiuscole sono",maiuscole)
print("le minuscole sono",minuscole)
    