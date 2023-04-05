dante="Nel mezzo del cammin di nostra vita \nmi ritrovai per una selva oscura,\nché la diritta via era smarrita" #\n serve per andare a capo
print(dante)	
daCercare=input("Cosa vuoi cercare?")		#chiedo all'utente di inserire la stringa da cercare
contatore=dante.count(daCercare)
print("trovato:",contatore)