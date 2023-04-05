numero1=5.0
numero2=2.5

print("PRIMA DEL CASTING")
print("numero1 =",numero1,"tipo:",type(numero1))
print("numero2:",numero2,"tipo:",type(numero2))
print("La loro somma è:",numero1+numero2)

#mettendo un tipo seguito da una variabile o qualcosa tra le parentesi si farà un casting
numero1=int(numero1)       #TIPO(COSA_CONVERTIRE_IN_TIPO)
numero2=int(numero2)

print("DOPO DEL CASTING A INT")
print("numero1 =",numero1,"tipo:",type(numero1))
print("numero2:",numero2,"tipo:",type(numero2))         #convertendo un float farà perdere la parte decimale
print("La loro somma è:",numero1+numero2)               #la somma sarà un numero int senza parte decimale

#la conversione di un numero in una stringa 
numero1=str(numero1)       #non verrà quindi più trattato come se fosse un numero
numero2=str(numero2)

print("CASTING DA NUMERO A STRING")
print("numero1 =",numero1,"tipo:",type(numero1))
print("numero2:",numero2,"tipo:",type(numero2))
#la somma di due stringhe darà la loro unione ovvero la concatenazione
print("La loro somma è:"+numero1+numero2)      #essendo una stringa, dobbiamo usare il + anche per concatenarla/sommarla al messaggio stampato anch'esso una stringa