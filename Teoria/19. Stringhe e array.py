a = "Hello, World!"
print(a)
print("La stringa è lunga",len(a))      #come per gli array, con len posso ottenere la lunghezza di una stringa

#in verità una stringa è un array di char/caratteri e segue la stessa regola per gli array
print("Ecco tutti i caratteri della stringa presi singolarmente")

indice=0        #userò questo indice per numerare i caratteri nel for sottostante

for x in a:     #scrorro tutti gli elementi della stringa/array di char. parte da 0 perchè il primo elemento di un array sta all'indice 0
  print(indice,")",x)      #stampo tutti gli elementi della stringa preceduto da un'etichetta che indica l'indice
  indice+=1                 #incremento l'indice

