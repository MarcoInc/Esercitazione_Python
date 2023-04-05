latte=float(input("quanto costa il latte?"))
pane=float(input("quanto costa il pane?"))
pasta=float(input("quanto costa la pasta?"))
carote=float(input("quanto costano le carote?"))
acqua=float(input("quanto costa l'acqua?"))
print("latte:",latte)
print("pane:",pane)
print("pasta:",pasta)
print("carote:",carote)
print("acqua:",acqua)
totale=latte+pane+pasta+carote+acqua
print("totale:",totale)
portafoglio=float(input("quanto hai?"))
if portafoglio<totale:
    print("mancano soldi")
elif portafoglio>=totale:
    print("il resto è ",portafoglio-totale)