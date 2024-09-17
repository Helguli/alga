# lokális változó függvényen belül
print("----------------lokális változó függvényen belül-------------------")
def lokalis_valtozo(): # függvényen belül lokális hatókör
    x = 12  # függvényen belül látható, érhető el az x, y és eredmeny változó
    y = 25  # csak a függvény idejére ÉL utána törlődik a memóriából
    eredmeny = x + y
    print("Az {0} + {1} eredménye: {2}".format(x, y, eredmeny))

for i in range(1,3):
    print("i érték (for-on belül): ",i)
print("i érték (for-on kívül): ",i) # globális hatókör - i

lokalis_valtozo() # függvény hívása
print(x, y, eredmeny)  #hibát jelez, függvényen kívül nem érhetőek el a belső változók

