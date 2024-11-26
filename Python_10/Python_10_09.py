import os
os.system('cls')

nevek=["Jancsi","Béla","Juliska","Jenő","Aladár","Jeromos"]

Jbetusok=filter(lambda nev : nev[0]=='J',nevek)
print("A J kezdőbetűs nevek: ",list(Jbetusok))

Jbetusok2=[nev for nev in nevek if nev[0]=='J'] # listaértelmezéssel
print("A J kezdőbetűs nevek: ",list(Jbetusok2)) 

