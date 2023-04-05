stringa=input("Inserisci una stringa")
stringa2=("")
for i in reversed(range(len(stringa))):
    stringa2+=stringa[i]
    
if stringa==stringa2:
    print("Palindromo")
else:
    print("Non palindromo")
    