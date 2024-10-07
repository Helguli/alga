#!/usr/bin/env python

# Létrehozunk egy halmazt
gyumolcsok = {"alma", "banán", "cseresznye", "dinnye", "eper"}

# Írjuk ki a halmaz elemeinek számát!
len(gyumolcsok)

# Az elemek nem indexelhetők.
#print(gyumolcsok[1])

# Menjünk végig az elemeken!
for x in gyumolcsok:
    print(x)

# Halmaz tagság
# Nézzük meg, benne van-e a dinnye a halmazban!
# Nézzük meg, benne van-e a barack a halmazban!
# Nézzük meg, nincs-e benne a barack a halmazban!
print("dinnye" in gyumolcsok) # True
print("barack" in gyumolcsok) # False
print("barack" not in gyumolcsok) # True

# Halmazműveletek
# Vegyük a zöldség és gyümölcs halmaz unióját!
zoldsegek = {"krumpli", "répa", "sütőtök"}
novenyek = gyumolcsok.union(zoldsegek)
novenyek2 = gyumolcsok | zoldsegek
print(novenyek)

# Vegyük a gyümölcs és déli gyümölcs halmaz metszetét!
deli_gyumolcsok = {'citrom', 'banán', 'narancs', 'mangó'}
metszet = gyumolcsok.intersection(deli_gyumolcsok)
metszet2 = gyumolcsok & deli_gyumolcsok
print(metszet)

# Vegyük a gyümölcs és déli gyümölcs halmaz különbségét!
kulonbseg = gyumolcsok.difference(deli_gyumolcsok)
kulonbseg2 = gyumolcsok - deli_gyumolcsok
print(kulonbseg)

# Nézzük meg, hogy a déli gyümölcs halmaz részhalmaza-e a gyümölcs halmaznak
print("Részhalmaz:", deli_gyumolcsok.issubset(gyumolcsok))
print("Részhalmaz:", deli_gyumolcsok <= gyumolcsok)
# A gyümölcs halmaz tartalmazza-e a déli gyümölcs halmazt.
# Ezzel ugyanazt nézzük meg, mint az előbb.
print("Tartalmazó halmaz:", gyumolcsok.issuperset(deli_gyumolcsok))
print("Tartalmazó halmaz:", gyumolcsok >= deli_gyumolcsok)

# Módosítás
# A halmaz összetétele módosítható
# Egy adott elem értéke nem írható át, viszont kivehetőek, berakhatóak elemek.

# Adjuk hozzá a halmazhoz a kedvenc gyümölcsünket!
gyumolcsok.add("barack")
# Vegyük ki a halmazból a nem finom gyümölcsöt!
gyumolcsok.remove("dinnye")
print(gyumolcsok)


# Lista metódusok
# Adjuk hozzá a szedret és a citromot a gyümölcs listához!
print(gyumolcsok)

# Vegyük ki a narancsot és a mangót a déli gyümölcs listából!
print(deli_gyumolcsok)

# Nézzük meg, részhalmaza-e a déli gyümölcs halmaz a másiknak!

# Vonjuk ki a déli gyümölcsöket a gyümölcs halmazból!

# Fűzzük össze a gyümölcs listát egy sztringgé, vesszővel elválasztva!
koz = ", "
s = koz.join(gyumolcsok)
print(s)

