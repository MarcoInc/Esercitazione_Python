import random
morraAvversario=["carta","forbice","sasso"]
mossaAvversario=morraAvversario[random.randint(0,3)]
tuaMossa=input("Inserisci carta , forbice o sasso")
print("L'avversario ha scelto",mossaAvversario)
#vincita
if tuaMossa == "carta" and mossaAvversario == "forbice":
    print("Hai vinto")
if tuaMossa == "forbice" and mossaAvversario == "sasso":
    print("Hai vinto")
if tuaMossa == "sasso" and mossaAvversario == "carta":
    print("Hai vinto")
#perdita
if tuaMossa == "forbice" and mossaAvversario == "carta":
    print("Hai perso")
if tuaMossa == "sasso" and mossaAvversario == "forbice":
    print("Hai perso")
if tuaMossa == "carta" and mossaAvversario == "sasso":
     print("Hai perso")
#parità
if tuaMossa == "forbice" and mossaAvversario == "forbice":
    print("Pareggio")
if tuaMossa == "sasso" and mossaAvversario == "sasso":
     print("Pareggio")
if tuaMossa == "carta" and mossaAvversario == "carta":
     print("Pareggio")

