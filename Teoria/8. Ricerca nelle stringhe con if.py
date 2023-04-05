dante="Nel mezzo del cammin di nostra vita \nmi ritrovai per una selva oscura,\nché la diritta via era smarrita" #\n serve per andare a capo
print(dante)	
daCercare=input("Cosa vuoi cercare?")		#chiedo all'utente di inserire la stringa da cercare
if daCercare in dante:						#se la parola da cercare sta nella stringa dante
    print("Parola trovata")					#se if da esito true stampa che l'ha trovata
    print("indice:",dante.index(daCercare)) #restituisce il primo indice dove ha trovato la stringa daCercare nella stringa dante