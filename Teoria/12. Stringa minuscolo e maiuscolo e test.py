stringa="ciao mondo"
print("1."+stringa)

#solo la prima lettera maiuscola
primaMaiscola=stringa.capitalize()
print("2."+primaMaiscola)

#tutta maiuscola
tuttaMaiuscola=stringa.upper()
print("3."+tuttaMaiuscola)

#tutta minuscola
tuttaMinuscola=tuttaMaiuscola.lower()
print("4."+tuttaMinuscola)

#test se è minuscolo
print("La 4. è minuscola?",tuttaMinuscola.islower())
print("La 3. è minuscola?",tuttaMaiuscola.islower())

#test se è maiuscola
print("La 4. è maiuscola?",tuttaMinuscola.isupper())
print("La 3. è maiuscola?",tuttaMaiuscola.isupper())


