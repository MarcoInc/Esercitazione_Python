anno=int(input("inserisci un anno"))
if anno%4==0 and anno%100!=0:
    print("anno bisestile")
elif anno%400==0:
    print("anno bisestile")
else:
    print("non bisestile")
    