#ordinare i numeri consiste nel mettere i più piccoli a sinistra e via via a destra quelli più grandi
lista = [2,1530, 4,-12, 3,-50, 0, 5, 11, 10,100]    #creo un array di numeri
lista.sort()        #la funzione automaticamente ordinerà lo stesso array, modificandolo
for i in range(len(lista)):     #stampo il risultato
    print(lista[i])
    
#è possible estrarre il max e il min senza if e for
print("Max", lista[0])                  #il min sarà il primo elemento
print("Min",lista[len(lista)-1])        #il max sarà l'ultimo elemento