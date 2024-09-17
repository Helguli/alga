def osszeg(*szamok):
    ossz = 0
    for szám in szamok:
        # összegezzük a szamok értékeit az ossz változóba
    return ossz

print("A számok összege: osszeg(1, 2, 3, 4)) # keressük meg a szintaktikai hibát

def osszefuz(*szinek, sep="/"):
    # írjuk ki a szinek változó típusát
    return sep.join(szinek)

print("Színek :",osszefuz("lila","kek","zold"))
print("Színek(,) :",osszefuz("lila","kek","zold",sep=","))

def szemely_adatok(**adatok):
    # írjuk ki az adatok változó típusát
    for kulcs, ertek in adatok.items():
        print(f"{kulcs}: {ertek}")

# szemely_adatok feltöltése értékekkel

