primo=float(input("Inserisci il primo numero: "))
secondo=float(input("Inserisci il secondo numero: "))

print("Somma:",primo+secondo)   
print("Sottazione:",primo-secondo)   
print("Prodotto:",primo*secondo)    
print("Divisione:",primo/secondo)    
print("Divisione intera:",int(primo/secondo))    
print("Resto divisione:",primo%secondo)        
print("Media:",(primo+secondo)/2)   
print(primo, "elevato a",secondo,"fa:",primo**secondo)      
print("Il",primo,"% di",secondo,"è:",(primo/100)*secondo)  

print(primo,"e",secondo,"sono uguali?",primo==secondo)
if primo==secondo:                      
    print("Sono uguali")
else:
    print("Sono diversi")