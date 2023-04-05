nomi=[]
print("inserisci nomi")
for i in range(0,5):
    nomi.append(input())
lunmax=len(nomi[0])
for i in range(0,5):
    if len(nomi[i])>=lunmax:
        lunmax=len(nomi[i])
        stringalunga=nomi[i]

print("il nome più lungo è:"+stringalunga)


        
        

