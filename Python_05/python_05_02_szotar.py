#!/usr/bin/env python

# Létrehozunk egy szótárat, amely gyümölcsöket és azok árait tartalmazza.
gyumolcsok = {
    "alma": 150,
    "banán": 200,
    "cseresznye": 300,
    "dinnye": 500,
    "eper": 400
}

# Írjuk ki a szótár elemeinek számát!
print(len(gyumolcsok))

# Szótár tagság
# Nézzük meg, benne van-e a dinnye a szótárban!
# Nézzük meg, benne van-e a barack a szótárban!
print("dinnye" in gyumolcsok)  # True
print("barack" in gyumolcsok)  # False

# A keys() függvény: Kiírja a szótár összes kulcsát.
print("Gyümölcsök kulcsai (keys):", gyumolcsok.keys())

# A values() függvény: Kiírja a szótár összes értékét.
print("Gyümölcsök árai (values):", gyumolcsok.values())

# Az items() függvény: Kiírja a szótár összes kulcs-érték párját.
print("Gyümölcsök kulcs-érték párok (items):", gyumolcsok.items())

# Menjünk végig a kulcs-érték párokon az items() használatával:
for gyumolcs, ar in gyumolcsok.items():
    print(f"A(z) {gyumolcs} ára: {ar} Ft")

# 4. A get() függvény: Biztonságosan adja vissza egy adott kulcs értékét, ha létezik.
# Ha a kulcs nem található a szótárban, akkor a második paraméterrel megadott alapértelmezett értéket adja vissza (vagy None-t, ha nincs megadva).
print("A banán ára (get):", gyumolcsok.get("banán"))  # 200 Ft
print("A barack ára (get):", gyumolcsok.get("barack", "Nincs ilyen gyümölcs"))  # Nincs ilyen gyümölcs

# Szótárhoz hozzáadás
# Adjuk hozzá a kedvenc gyümölcsünket a szótárhoz!
gyumolcsok["barack"] = 250
print(gyumolcsok)

# Adjuk hozzá a körtét is a szótárhoz a get függvény segítségével!
if gyumolcsok.get("körte") is None:
    gyumolcsok["körte"] = 250
print("Frissített gyümölcsök:", gyumolcsok)


# Szótárból elem törlése
# Vegyük ki a nem finom gyümölcsöt a szótárból!
#del gyumolcsok["dinnye"]
gyumolcsok.pop("dinnye")
print(gyumolcsok)

# Egy másik szótár létrehozása zöldségekkel és azok árával
zoldsegek = {
    "krumpli": 180,
    "répa": 100,
    "sütőtök": 350
}

# Egyesítsük a gyümölcs és zöldség szótárakat egy nagyobb szótárba!
novenyek = gyumolcsok | zoldsegek
print("Növények:", novenyek)

# Egy adott gyümölcs árának módosítása
# Módosítsuk az eper árát 450 Ft-ra!
gyumolcsok["eper"] = 450
print("Módosított árak:", gyumolcsok)

# Szótárból sztring fűzése: gyümölcsnevek összefűzése vesszővel elválasztva
koz = ", "
s = koz.join(gyumolcsok.keys())
print("Gyümölcsök:", s)
