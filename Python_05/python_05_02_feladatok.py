#!/usr/bin/env python

# Hozz létre egy szótárat a kedvenc gyümölcseidről és azok árairól!
gyumolcsok = {}

# Kérj be egy gyümölcs nevét a felhasználótól, majd írd ki az árát, ha benne van!

# Másold le a szótárat!

# Adj hozzá egy új elemet az új szótárhoz, amit a felhasználó ír be!

# Nézd meg, változott-e az eredeti szótár!

# Hogy lehet elérni, hogy az eredeti szótár változzon/ne változzon?

# Rendezd a szótárat kulcsok szerint csökkenő sorrendbe!

# Készíts egy szótárat, ami tartalmazza a gyümölcs szótár és az alábbi szótár összes elemét!
tobb_gyumolcs = {
    "szőlő": 300,
    "barack": 250,
    "alma": 150,
    "banán": 200,
    "cseresznye": 300,
    "citrom": 180,
    "ananász": 400,
    "szilva": 220
}

osszes_gyumolcs = dict()
print("Összes gyümölcs:", osszes_gyumolcs)

# Távolítsd el a duplikált kulcsokat!
# Ez már megtörtént az összevonás során, mert a szótárak automatikusan felülírják a meglévő kulcsokat.

# Rendezd a szótárat értékek szerint növekvő sorrendbe!
rendezett_ertek_szerint = dict()
print("Rendezett gyümölcsök ár szerint:", rendezett_ertek_szerint)

# Fűzd össze a kulcsokat egy sztringgé a következő elválasztóval.
koz = " -- "
gyumolcs_string = ""
print("Gyümölcsök összefűzve:", gyumolcs_string)
