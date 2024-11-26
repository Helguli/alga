import os
gyumolcsok = ["alma", "körte", "ananász", "cseresznye", "dió"]

iterator_objektum=map(len,gyumolcsok) # a gyumolcsok lista minden elemére
                                      # végrehajtódik a len függvény

os.system('cls')
print(list(iterator_objektum)) # az iterátor objektumot listává alakítjuk előbb
print([len(x) for x in gyumolcsok]) # ugyanaz megoldható listaértelmezéssel
 
 