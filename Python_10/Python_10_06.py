def Szorzo(n):
  return lambda x : x * n

triplazo = Szorzo(3) # A Szorzo egy olyan névtelen függvényt ad vissza, amely
                     # egy paramétert vár, és annak visszaadja a 3-szorosát. Ezt 
                     # képviseli a triplazo függvény.
print(triplazo(10))
print(Szorzo(4)(12)) # közvetlenül hívjuk a 4-gyel szorzó névtelen függvényt 
                     # a 12 paraméterrel
print(Szorzo(4)(Szorzo(4)(12))) # a 4-gyel szorzo névtelen függvény paraméterét
                                # a 12-t paraméterül kapó 4-gyel szorzó névtelen
                                # függvény állítja elő
