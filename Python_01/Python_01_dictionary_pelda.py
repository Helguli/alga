szotar = {"paard": "ló","ik": "én","twee": 2}
print("Kiírás: ", szotar)
print("Mérete: ", len(szotar)) # visszaadja a szótár méretét
print("Értékpárt ad vissza: ik -->", szotar["ik"])

szotar["twee"] = "kettő" # módosítja az értéket (2-->kettő)
szotar["appfel"] = "alma"  # új elem hozzáadása
szotar.pop("ik")  # ik elempár törlése
print("Módosított szótár: ", szotar)

szotar.popitem() # utoljára hozzáadott törlése
print("Utoljára hozzáadott elem törlés: ", szotar)

