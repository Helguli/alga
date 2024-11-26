import os
def Osszead(a,b):
    return a+b

def Fuggveny(fuggvenypar,x,y):
    return fuggvenypar(x,y)

os.system('cls')
print(Fuggveny(Osszead,10,8))
