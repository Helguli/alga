#!/usr/bin/env python

# Létrehozunk egy listát
gyumolcsok = ["alma", "banán", "cseresznye", "dinnye", "eper"]

# Írjuk ki a lista hosszát!
len(gyumolcsok)

# Menjünk végig az elemeken!
for i in range(len(gyumolcsok)):
    print(gyumolcsok[i])

for x in gyumolcsok:
    print(x)

# Ha az érték mellett szükség van az indexre is, használható az enumerate, ami index-érték párokat ad.
for index, gyumolcs in enumerate(gyumolcsok):
    print(index, gyumolcs)

# Lista tagság
# Nézzük meg, benne van-e a dinnye a listában!
# Nézzük meg, benne van-e a barack a listában!
# Nézzük meg, nincs-e benne a barack a listában!
print("dinnye" in gyumolcsok) # True
print("barack" in gyumolcsok) # False
print("barack" not in gyumolcsok) # True

# Lista műveletek
# Fűzzük össze a zöldség és gyümölcs listát egybe!
zoldsegek = ["krumpli", "répa", "sütőtök"]
novenyek = gyumolcsok + zoldsegek
print(novenyek)

# Ismételjük meg a gyümölcs listát ötször!
sok_gyumolcs = gyumolcsok * 5
print(sok_gyumolcs)

# Részlista
# Írassuk ki a ['banán', 'cseresznye'] részlistát!
# Írassuk ki az utolsó két elemből álló részlistát!
print(gyumolcsok[1:3])
print(gyumolcsok[-2:])

# Módosítás
# A lista elemei módosíthatók
# Írjuk át a banánt barackra!
gyumolcsok[1] = "barack"
print(gyumolcsok)
# Részlistát is lehet törölni, üres list hozzárendelésével
# Távolítsuk el a ['cseresznye', 'dinnye'] részlistát!
keves_gyumolcs = gyumolcsok[:]
keves_gyumolcs[2:4] = []
print(keves_gyumolcs)

# Objektumok és hivatkozások
# Az alábbi két listában ugyanazok az értékek szerepelnek.
# De vajon ugyanarra az objektumra hivatkoznak-e?
zoldsegek1 = ["krumpli", "répa", "sütőtök"]
zoldsegek2 = ["krumpli", "répa", "sütőtök"]
print("Egyenlő:", zoldsegek1 == zoldsegek2)
print("Ugyanaz:", zoldsegek1 is zoldsegek2)

# A válasz az, hogy nem.
# zoldsegek1 -> ["krumpli", "répa", "sütőtök"]
# zoldsegek2 -> ["krumpli", "répa", "sütőtök"]
#

# Ha egy változót egy másikhoz rendelünk hozzá, mindkettő mögött ugyanaz az objektum fog szerepelni.
# zoldsegek1                                 
#            \                              
#             _|                            
#             _ ["krumpli", "répa", "sütőtök"]
#              |                            
#            /                              
# zoldsegek2                               
zoldsegek3 = zoldsegek1
print("Ugyanaz:", zoldsegek1 is zoldsegek3)
# Ilyenkor bármelyik listát változtatjuk, az módosít a másikon.
zoldsegek1.append("káposzta")
print(zoldsegek3)

# Le tudunk másolni egy listát úgy, hogy ne ugyanarra az objektumra hivatkozznak.
# Ezt klónozásnak nevezzük.
zoldsegek4 = zoldsegek3[:]
print(zoldsegek4)

# Lista metódusok
# Adjuk hozzá a szedret a gyümölcs listához!
gyumolcsok.append("szeder")
print(gyumolcsok)

# Szúrjuk be a citromot a lista elejére!
gyumolcsok.insert(0, "citrom")
print(gyumolcsok)

# Hányszor szerepel az alma a listában?
print("Az alma szó ennyiszer szerepel:", gyumolcsok.count("alma"))

# Fordítsuk meg a listát!
gyumolcsok.reverse()
print(gyumolcsok)

# Rendezzük sorba a listát!
gyumolcsok.sort()
print(gyumolcsok)

# Rendezzük sorba a listát karakterek száma alapján csökkenő sorrendbe!
gyumolcsok.sort(reverse = True, key = lambda x: len(x))
print(gyumolcsok)

# Fűzzük össze a gyümölcs listát egy sztringgé, vesszővel elválasztva!
koz = ", "
s = koz.join(gyumolcsok)
print(s)

# Válasszuk szét az alábbi sztringet a szóközöknél!
vers = "Erdőszélen nagy a móka, mulatság, iskolába gyűlnek mind a nyulacskák."
szavak = vers.split(" ")
print(szavak)

# Mátrixok
mx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("A mátrix első sora: ", mx[0])
print("A mátrix utolsó sorának első eleme: ", mx[2][0])

