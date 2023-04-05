numeri=[5,151,100,15,43,20,1,150]       #raccolta di numeri
max=numeri[0]           #inizializzo il primo elemento come max
min=numeri[0]           #inizializzo il primo elemento come min
for i in numeri:        #i sarà l'elemento che verrà scorso dentro numeri e via via passa all'elemento successivo, quindi alla prima ripassata i sarà uguale al primo elemento
    if(i>max):          #se l'attuale max ha un numero più grande,
        max=i           #questo sarà il nuovo max
    if(i<min):          #se l'attuale min ha un numero più piccolo,
        min=i           #questo sarà il nuovo min
print("Min:",min)       #stampo i risultati
print("Max:",max)
