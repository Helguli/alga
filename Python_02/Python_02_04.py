def osszeg_it(n):  # iteratív megoldás
    eredmeny = 0
    # for ciklus végrehajtási száma n (1-től induljon)
        # eredmenyhez adjuk hozzá az ciklusváltozó (i) értékét
    return eredmeny

def osszeg_rek(n):  # rekurzív megoldás
    if n == 0:
        return 0
    # visszatérési értéken belül a függvény rekurzív hívása értékkel

szam = int(input("Kérem adja meg a számot: ")) # ellenőrzés nélküli beolvasás, számot kell megadni
osszeg = osszeg_it(szam)
print("Az első {0} természetes szám összege iteratív függvénnyel {1}.".format(szam, osszeg))
osszeg2 = osszeg_rek(szam)
print("Az első {0} természetes szám összege rekurzív függvénnyel {1}.".format(szam, osszeg2))
