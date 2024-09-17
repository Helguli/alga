print("\n-----------------------globális változó------------------------------")
x = 5
y = 8
def globalis_valtozo():
    x = 500   # lokális változó, függvényen belül, nem a külső x-el egyenlő
    # global kulcsszó használatával globális hatókörű lesz a változó
    y = 800   # felülírja az y értékét
    # írjuk ki x,y értékét

globalis_valtozo()
# írjuk ki x,y értékét

