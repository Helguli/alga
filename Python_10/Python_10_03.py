def Osszead(a,b):
    return a+b

lista=["valami",Osszead,12,"alma"]
print(lista[1])        # a függvény memóriabeli kezdőcíme
print(lista[1](12,23)) # a függvény hívása és az eredmény kiíratása

