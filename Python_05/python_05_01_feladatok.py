#!/usr/bin/env python

# Halmaz létrehozása
# Az elemeket kapcsos zárójelek között soroljuk fel.
# Látjuk, hogy a 21-es szám csak egyszer fog szerepelni a halmazban.
harommal_oszthato = {0, 3, 6, 9, 12, 15, 18, 21, 21}
print(harommal_oszthato)
# Set comprehension
neggyel_oszthato = {x for x in range(0,20) if x % 4 == 0}
print(neggyel_oszthato)

# Hozz létre egy halmazt, ami tartalmazza a páros számokat 0-tól 20-ig!
paros = set()

# Add hozzá a páros számokat tartalmazó halmazhoz a 22 számot is!
print(paros)

# Ellenőrizd, hogy részhalmaza-e a néggyel osztható számok halmaza a páros számok halmazának!

# Vond ki a páros számokból a néggyel oszthatókat, és írd ki az eredmény halmazt!
print("Néggyel nem osztható páros számok:")

# Készíts egy hattal osztható halmazt, madj tedd bele az annak megfelelő számokat!
# Tipp: páros és hárommal osztható számok metszete.
print("Hattal osztható számok: ")

# Írd ki a hárommal és néggyel osztható számok unióját!
print("Hárommal vagy néggyel osztható számok:")
